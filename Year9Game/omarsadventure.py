import termcolor 
import random
import playsound

border = "-----------------------------------------------------------------"


# playsound.playsound('littledarkage.mp3', block = False)





 
def invalid(rand):
    if rand == 1:
        print ("That is not a valid command.")
    if rand == 2:
        print ("That command doesn't seem right...")
    if rand == 3: 
        print ("Try that command again please!")
    

titletext = termcolor.colored ("Omar's Adventure",'red',attrs = ['bold','underline'])
print (border)
print (f"Welcome to \n{titletext}\n(Type \"t\" for tutorial or \"play\" to start playing!)")


correct1 = False
while not correct1:
    tutorialinput = input ()

    if "t" in tutorialinput.lower():
        print (border)
        helptext = termcolor.colored ("Remember that you can ALWAYS TYPE \"HELP\" during the game to pop this text back up!", 'red', attrs = ['bold'])
        print (f"To play this game you must ender commands when asked! \nFor example, if I ask \"Do you like Omar\" a proper command would be to enter \"yes\". \nDon't worry, if enter an invalid command i'll let you know! \n{helptext}\n\nHere is a list of all the possible commands: \n\nyes\nno\n\n\nType \"play\" to start playing the game.")
        correct1 = True
        correct2 = False
        while not correct2:
            tutorialinput2 = input()    
            if "p" in tutorialinput2.lower():
                print (border)
                correct2 = True
            else:
                print (border)
                invalid(random.randint(1,3))
            
    elif "p" in tutorialinput.lower():
        print (border)
        correct1 = True
    
    else: 
        print (border)
        invalid(random.randint(1,3))

print ("Type \"1\" to play through Mrs. Rogers's story!\nType \"2\" to play through Daniel's story! ")
correct3 = False
while not correct3:
    gameselectinput = input ()
    if "1" in gameselectinput: 
        print (border)
        correct3 = True
        correct4 = False
        print ("While you're doing homework, you hear news that Mrs. Rogers, your neighbour who seems to hate everything you do, had an accident and fell. \nYour mom tells you that for the next few days you'll have to help her cook for Mrs. Rogers. Should you still help her if she \ndislikes you and your culture?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ruin her meal by pouring salt in it.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to cook her the best meal that you can.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to refuse to cook her the meal.")
        while not correct4:
            choice1 = input()
            if "1" in choice1:
                print (border)
                print ("She hates you and your family even more now...\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ruin her meal by pouring salt in it.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to cook her the best meal that you can.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to refuse to cook her the meal.")
            
            elif "2" in choice1:
                print (border)
                print ("She ate the meal and told your mom \"It was okay\".\nYou might not have gotten the reaction you wanted, but it was still the right thing to do.\nIt takes time to get people to warm up to you!\n\nType \"next\" to continue!")
                correct4 = True
                correct5 = False
                while correct5 == False:
                    choice2 = input()
                    if "n" in choice2.lower():
                        correct5 = True
                    else:
                        print (border)
                        invalid(random.randint(1,3))
            elif "3" in choice1:
                print (border)
                print ("Your mom cooked her meal in a rush and it didn't look that good. When you went to pick it up from Ms. Rogers she grumbled at you.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ruin her meal by pouring salt in it.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to cook her the best meal that you can.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to refuse to cook her the meal.")
            else: 
                print (border)
                invalid(random.randint(1,3))
            
    elif "2" in gameselectinput:
        print (border)
        print ("Daniel Chapter Filler")
        correct3 = True
    else: 
        print (border)
        invalid(random.randint(1,3))
        


    





