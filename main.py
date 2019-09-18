from PIL import Image, ImageDraw, ImageFont
import random, json, argparse, os, sys

parser = argparse.ArgumentParser()
parser.add_argument("-m", help="migrate config file",action="store_true")
parser.add_argument("-add", help="add poem",action="store_true")
parser.add_argument("-rm", help="delete poem",action="store_true")
parser.add_argument("-l", help="delete poem",action="store_true")
args = parser.parse_args()

configPath = "config.json"
poemPath = "res/poem-txt"
BGPath = "res/background-imgs"

poemList = os.listdir(poemPath)
BGList = os.listdir(BGPath)

def ConfigManager(command, Num):
    poemList = os.listdir(poemPath)
    BGList = os.listdir(BGPath)

    if(command == "add"):
        data = {"DATASET": {"PoemNum": len(poemList), "BGNum": len(BGList)}}
        with open(configPath, "w") as write_file:
            json.dump(data, write_file)
    elif(command == "del"):
        print("delete target")
    
if args.m:
    data = {"DATASET": {"PoemNum": len(poemList), "BGNum": len(BGList)}}

    with open(configPath, "w") as write_file:
        json.dump(data, write_file)

    print("-------------DATASET Config-------------")
    print("PoemNum : " + str(data['DATASET']['PoemNum']))
    print("BGNum : " + str(data['DATASET']['BGNum']))
    print("----------------------------------------")

    sys.exit()

elif args.add:
    print("-----------------Create New poem------------------")
    NewPoemTitle = input("시 제목을 입력해주세요:")
    NewPoemAuthor = input("시인의 이름을 입력해주세요:")
    NewPoemContent = []
    tmp = []
    while (True):
        tmp = ""
        tmp = input("본문 입력('@'를 입력하여 본문 입력을 끝냅니다.) : ")
        if(tmp == "@"): 
            break
        NewPoemContent.append(tmp)

    print("새로운 시 제목 :"+ str(NewPoemTitle))
    print("새로운 시인:"+str(NewPoemAuthor))
    print("새로운 시 본문:"+str(NewPoemContent))
    
    poemList = os.listdir(poemPath) 

    newPoem = open(poemPath+"/poem("+str(len(poemList)+1)+").txt", "w", encoding='UTF8')

    newPoem.write(NewPoemTitle+"\n")
    newPoem.write(NewPoemAuthor+"\n")
    #print()
    newPoem.write(str('\n'.join(NewPoemContent)))

    ConfigManager("add",1)
    #print(type(NewPoemContent))
    print("-------------New poem added to list---------------")
    sys.exit()

elif args.rm:
    poemList = os.listdir(poemPath)
    rmPoemPath = "res/poem-txt/poem("+str(len(poemList))+").txt"
    rmPermission = input("'"+rmPoemPath+"' 를 정말 지우시겠습니까? y/n ")

    if rmPermission == "y" or rmPermission == "Y":
        print(("'"+rmPoemPath+"' 를 성공적으로 삭제했습니다."))
        os.remove(rmPoemPath)
        sys.exit()
    elif rmPermission == "n" or rmPermission == "N":
        print("삭제 취소")
        sys.exit()
    else:
        print("다른Command를 입력하셨습니다.")
        sys.exit()

    sys.exit()

elif args.l:
    for x in range(len(poemList)):
        poemPath = "res/poem-txt/poem("+str(x+1)+").txt"
        f = open(poemPath, "r", encoding='UTF8')
        readPoemTitle = f.readline()
        f.close()
        print("poem("+str(x+1)+").txt: "+readPoemTitle)
    sys.exit()

WHITE = (255,255,255)

with open('config.json') as json_file:
    data = json.load(json_file)

    PoemNum = data['DATASET']['PoemNum']
    BGNum =  data['DATASET']['BGNum']

for x in range(PoemNum):
    fontPath = "res/font-files/a시나리오.ttf"
    poemPath = "res/poem-txt/poem("+str(x+1)+").txt"
    #print("read file : " + filename)
    f = open(poemPath, "r", encoding='UTF8')

    backgroundImgPath = "res/background-imgs/"+str(random.randrange(1,BGNum))+".png"
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
    f.close()
    backgroundImg.save(targetPath)
    print("[LOG]Image Saved!")
    print("--------------------------------")
