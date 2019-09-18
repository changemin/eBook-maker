from PIL import Image, ImageDraw, ImageFont

WHITE = (255,255,255)

for x in range(2):
    filename = "../poem-txt/poem("+str(x+1)+").txt"
    #print("read file : " + filename)
    f = open(filename, "r", encoding='UTF8')

    poemTitle = f.readline()
    poemAuthor = f.readline()
    poemContent = f.read()

    print(str(x+1) + "번째 시 제목:" + poemTitle) #title of the poem
    print("시인:" + poemAuthor) #author of the poem
    #print(poemContent) #content

    img = Image.new('RGB', (1000, 1000), color = (0,0,0,0))

    titleFont = ImageFont.truetype('../font-files/KoPubDotumBold.ttf', 50)
    authorFont = ImageFont.truetype('../font-files/KoPubDotumBold.ttf', 20)
    contentFont = ImageFont.truetype('../font-files/KoPubDotumBold.ttf', 30)

    d = ImageDraw.Draw(img)
    d.text((100,100), poemTitle, font=titleFont, fill=WHITE)
    d.text((100,160), poemAuthor, font=authorFont, fill=WHITE)
    d.text((100,240), poemContent, font=contentFont, fill=WHITE)

    targetPath = "../result/poemResult("+ str(x) +").png"
    img.save(targetPath)
    print("[LOG]Image Saved!")