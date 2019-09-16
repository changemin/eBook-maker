#import string

for x in range(1):
    filename = "poem-txt/poem("+str(x+1)+").txt"
    print(filename)
    f = open(filename, "r", encoding='UTF8')
    print("시 제목 : " + f.readline()) #title of the poem
    print("시인 : " + f.readline()) #author of the poem
    print(f.read()) #content