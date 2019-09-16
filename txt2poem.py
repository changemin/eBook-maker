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