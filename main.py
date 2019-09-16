from PIL import Image, ImageDraw, ImageFont
import random

WHITE = (255,255,255)

for x in range(2):
    fontPath = "res/font-files/a시나리오.ttf"
    poemPath = "res/poem-txt/poem("+str(x+1)+").txt"
    #print("read file : " + filename)
    f = open(poemPath, "r", encoding='UTF8')

    backgroundImgPath = "res/background-imgs/"+str(random.randrange(1,4))+".png"
    backgroundImg = Image.open(backgroundImgPath)

    poemTitle = f.readline()
    poemAuthor = f.readline()
    poemContent = f.read()

    print(str(x+1) + "번 시 제목:" + poemTitle) #title of the poem
    print("시인:" + poemAuthor) #author of the poem
    #print(poemContent) #content

    titleFont = ImageFont.truetype(fontPath, 80)
    authorFont = ImageFont.truetype(fontPath, 35)
    contentFont = ImageFont.truetype(fontPath, 30)

    d = ImageDraw.Draw(backgroundImg)
    d.text((100,160), poemTitle, font=titleFont, fill=WHITE)
    d.text((550,260), poemAuthor, font=authorFont, fill=WHITE)
    d.text((100,360), poemContent, font=contentFont, fill=WHITE)

    d.line((90,320,640,320),fill=WHITE, width=1)

    targetPath = "result/poemResult("+ str(x+1) +").png"
    backgroundImg.save(targetPath)
    print("[LOG]Image Saved!")
    print("--------------------------------")