import sys,time

# for x in range(1):
#     filename = "../poem-txt/poem-master.txt"
#     print("read file : " + filename)
#     f = open(filename, "r", encoding='UTF8')

#     poemTitle = f.readline()
#     poemAuthor = f.readline()
#     newline = f.readline()
#     while(newline != '@'):
#         if newline == '@':
#             sys.exit()
#         print(newline)
#         newline = f.readline()
#         sleep(1)
#     #poemContent = f.read()

#     # print("시 제목:"+poemTitle) #title of the poem
#     # print("시인:"+poemAuthor) #author of the poem
#     # print(poemContent) #content

filename = "../poem-txt/poem-master.txt"
# with open(filename, 'r', encoding='UTF-8') as poemMaster:
#     while(True):
#         for line in poemMaster:
#             poemTitle = poemMaster.readline()
            
#             if '@' in line:
#                 #print(line)
#                 print("-----------------------")
#             elif '#' in line:
#                 sys.exit()
#             print(line)
f = open(filename, "r", encoding='UTF8')
while(True):
    newline = f.readline()
    if(newline == '@'):
        sys.exit()
    print(newline)