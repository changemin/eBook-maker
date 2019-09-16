from PIL import Image, ImageDraw, ImageFont
 
for x in range(1):
    filename = "poem-txt/poem("+str(x+1)+").txt"
    print("read file : " + filename)
    f = open(filename, "r", encoding='UTF8')

    poemTitle = f.readline()
    poemAuthor = f.readline()
    poemContent = f.read()

    print("시 제목:"+poemTitle) #title of the poem
    print("시인:"+poemAuthor) #author of the poem
    print(poemContent) #content

img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
 
fnt = ImageFont.truetype('font-files/KoPubDotumBold.ttf', 15)
d = ImageDraw.Draw(img)
d.text((10,10), poemTitle, font=fnt, fill=(255, 255, 0))
d.text((10,70), poemAuthor, font=fnt, fill=(255, 255, 0))
d.text((10,150), poemContent, font=fnt, fill=(255, 255, 0))

img.save('result/poemResult(1).png')