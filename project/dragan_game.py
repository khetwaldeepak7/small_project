import pyautogui  # 1 install pyautogui
# this is how we import the pillow package                    
#install pillow package
from PIL import Image,ImageGrab    # grab help to take the screenshot  
# 'Now to take the screenshot we wil use the function
import time
#as hit key inherating the function of key it so it can use all the method of key
def hit(key):  # hit is a function which will help to hit the key automatically,
    pyautogui.keyDown(key)
'''
def iscollide(data):

    for i in range(440,460):
        for j in range(407,430):
           if data[i,j] <100:  #beacuase we know the pixel of black isless than 100
               return True  # njo true return true kareyga
    return False


#def takescreenshot():
    #image=ImageGrab.grab()#  # inside imagegrab there is a method of name grab to grab the image
 # show is the function inside the imagegrab packagef
    #return image                              #takescreenshot() we can call it directly but it would be good to keep and call this function inside main


if __name__=='__main__':# stRT IDHR SEY HIOA MAIN MAI SEY   
    print("hie ur game will start in few second")
    time.sleep(2)# to keep some time in loading a program
        # to start the game we have to hit the key
        # so we will call the hit function
    hit("up")
while True:
    image=ImageGrab.grab().convert('L')
    data=image.load() # to take the picture in a array format
    # load huwa check karna hai kahi image repeat toh nhi ho rha hai,agar nhi toh
    if iscollide(data):# agar kahi par collide hota hai data toh fir niche ek function hit ko call kar do
          hit("up")    # toh hit function ko call karo,jo agument mai key leyga

'''


time.sleep(2)
image=ImageGrab.grab().convert('L')
data=image.load()
for i in range(445,460):  # starting number and ending number ke bich jitna gap rakheyga utna jada horizatanlly wah increase hoga
      for j in range(405,430):  # eska v same but vertically lage hoga
            data[i,j]=0  # becaue 0 is used for black color
            #because yeh btyega ki kha par caktas hai,becuase the color of the kakta is black
image.show()

 
    













'''
while True:
    pyautogui.keyDown("d")
    pyautogui.keyDown("e")
    pyautogui.keyDown("e")
    pyautogui.keyDown("p")
    pyautogui.keyDown("a")
    pyautogui.keyDown("k")
'''
