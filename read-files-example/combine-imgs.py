from PIL import Image

def main(): 
    try: 
        print("try in")
        #Relative Path 
        #Image on which we want to paste 
        img = Image.open("img-files/example/1.jpg")  
        print("Open first jpg")  
        #Relative Path 
        #Image which we want to paste 
        img2 = Image.open("img-files/example/2.jpg")  
        print("Open second jpg")
        img.paste(img2, (300, 300)) 
        print("paste imgs")
          
        #Saved in the same relative location 
        img.save("img-files/target/pasted_picture.jpg") 
        print("Paste Finished!")
          
    except IOError: 
        pass
        print("IOError")
  
if __name__ == "__main__": 
    main() 
  