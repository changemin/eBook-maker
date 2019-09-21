from PIL import Image, ImageDraw, ImageFont
import re
#ipath= u"./data/NCDC/上海/虹桥/9705626661750dat.txt"
 
text2print = "한국어 中國語"

img = Image.new('RGB', (1000, 1000), color = (73, 109, 137))
defaultFnt = ImageFont.truetype('font-files/나눔명조Bold', 50)
chineseFnt = ImageFont.truetype('font-files/KoPubDotumBold.ttf', 50)
d = ImageDraw.Draw(img)

cursorx = 50 
cursory = 50

for x in text2print:
    if u'\u4e00' <= x <= u'\u9fff':
        print(x+"is chinese")
        d.text((cursorx, cursory), x, font=chineseFnt, fill=(255, 255, 0))
        cursorx += 45
    else:
        print(x+"is not chinese")
        d.text((cursorx, cursory), x, font=defaultFnt, fill=(255, 255, 0))
        cursorx += 45

d.text((50, 150), text2print, font=defaultFnt, fill=(255, 255, 0))

# print(re.findall(r'[\u4e00-\u9fff]+', text2print))
# print(str(re.findall(r'[\u4e00-\u9fff]+', text2print)))
# print(type(re.findall(r'[\u4e00-\u9fff]+', text2print)))
# print(len(re.findall(r'[\u4e00-\u9fff]+', text2print)))

img.save('../../result/checkIfChinese.png')