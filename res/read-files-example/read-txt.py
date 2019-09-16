for x in range(3):
    filename = "text-files/"+str(x+1)+".txt"
    f = open(filename, "r", encoding='UTF8')
    print(f.read())
# f = open("text-files/1.txt", "r")
# print(f.read())