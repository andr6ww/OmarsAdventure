import termcolor 
import random
import playsound

border = "-----------------------------------------------------------------"


playsound.playsound('Little Dark Age.mp3', block = False)




 
def invalid(rand):
    if rand == 1:
        print ("That is not a valid command.")
    if rand == 2:
        print ("That command doesn't seem right...")
    if rand == 3: 
        print ("Try that command again please!")
    

titletext = termcolor.colored ("Omar's Adventure",'red',attrs = ['bold','underline'])
print (border)
print (f"Welcome to \n{titletext}\n(Type \"t\" for tutorial or \"g\" to get straight to the game!)")


num1 = 0
while num1 == 0:
    tutorialinput = input ()

    if "t" in tutorialinput.lower():
        print (border)
        helptext = termcolor.colored ("Remember that you can ALWAYS TYPE \"HELP\" during the game to pop this text back up!", 'red', attrs = ['bold'])
        print (f"To play this game you must ender commands when asked! \nFor example, if I ask \"Do you like Omar\" a proper command would be to enter \"yes\". \nDon't worry, if enter an invalid command i'll let you know! \n{helptext}\n\nHere is a list of all the possible commands: \n\nyes\nno\n\n\nType \"g\" to start the game")
        num1 =+ 1
        num2 = 0
        while num2 == 0:
            tutorialinput2 = input()    
            if "g" in tutorialinput2.lower():
                print (border)
                num1 =+ 1
                num2 =+ 1
            else:
                print (border)
                invalid(random.randint(1,3))
            
    elif "g" in tutorialinput.lower():
        print (border)
        num1 =+ 1
    
    else: 
        print (border)
        invalid(random.randint(1,3))

print ("Type \"1\" to play through Mrs. Rogers's story!\nType \"2\" to play through Daniel's story! ")
num4 = 0
while num4 == 0:
    gameselectinput = input ()
    if "1" in gameselectinput: 
        print (border)
        print ("While you're doing homework, you hear news that Mrs. Rogers, your neighbour who seems to hate everything you do, had an accident and fell. \nYour mom tells you that for the next few days you'll have to help her cook for Mrs. Rogers. Should you still help her if she \ndislikes you and your culture?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ruin her meal by pouring salt in it.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to cook her the best meal that you can.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to refuse to cook her the meal.")
        num4 += 1
        num5 = 0
        while num5 == 0:
            choice1 = input()
            if "1" in choice1:
                print (border)
                print ("filler 1")
                num5 += 1
            elif "2" in choice1:
                print (border)
                print ("filler 2")
                num5 += 1
            elif "3" in choice1:
                print (border)
                print ("filler 3")
                num5 += 1
            else: 
                invalid(random.randint(1,3))
    elif "2" in gameselectinput:
        print (border)
        print ("Daniel Chapter Filler")
        num4 += 1
    else: 
        print (border)
        invalid(random.randint(1,3))
        


    





