import termcolor 
import random
import playsound
import os

def clearConsole():
    clear = lambda: os.system('clear')
    clear()

clearConsole()

border = "-----------------------------------------------------------------"


playsound.playsound('oceandrive.mp3', block = False)






 
def invalid(rand):
    if rand == 1:
        print ("That is not a valid command.")
    if rand == 2:
        print ("That command doesn't seem right...")
    if rand == 3: 
        print ("Try that command again please!")
    

titletext = termcolor.colored ("Omar's Adventure",'red',attrs = ['bold','underline'])
print (border)
print (f"Welcome to \n{titletext}\n(Type \"tutorial\" for tutorial or \"play\" to start playing!)")


correct1 = False
while not correct1:
    tutorialinput = input ()

    if "t" in tutorialinput.lower():
        print (border)
        helptext = termcolor.colored ("Remember that you can ALWAYS TYPE \"HELP\" during the game to pop this text back up!", 'red', attrs = ['bold'])
        print (f"To play this game you must enter commands when asked! \nFor example, if I ask \"Do you like Omar\" a proper command would be to enter \"yes\". \nDon't worry, if enter an invalid command i'll let you know!")        
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
                        correct6 = False
                        print (border)
                        print ("Tonight your dad tells you that you're eating your favourite food. He also says that he wants to invite Mrs. Rogers but you're afraid that she'll ruin the mood of the dinner. Should you still attend?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to eat dinner when Mrs. Rogers is there.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to attend the dinner normally and be your playful self.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" attend the dinner but stay quiet and respectful, having less fun.")
                        while not correct6:
                            choice3 = input()
                            if "1" in choice3:
                                print (border)
                                print ("Mrs. Rogers finds out why you skipped dinner and walks out in the middle of dinner.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to eat dinner when Mrs. Rogers is there.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to attend the dinner normally and be your playful self.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" attend the dinner but stay quiet and respectful, having less fun.")
                            elif "2" in choice3:
                                print (border)
                                print ("Mrs. Rogers stays for the dinner but is weirded out by your behaviour.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to eat dinner when Mrs. Rogers is there.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to attend the dinner normally and be your playful self.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" attend the dinner but stay quiet and respectful, having less fun.")

                            elif "3" in choice3:
                                print (border)
                                print ("She enjoyed the meal.\nSometimes we have to take sacrifices for people.\nInstead of being your usual self, you stayed respectful and tried to make Mrs. Rogers as comfortable as possible!\n\nType \"next\" to continue!")
                                correct6 = True
                                correct7 = False
                                while not correct7:
                                    choice4 = input()
                                    if "n" in choice4.lower():
                                        correct7 = True
                                        correct9 = False
                                        print (border)
                                        print ("Mrs. Rogers seems to be warming up to you and your family but one night during dinner, she says something really mean about your culture. What should you do?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to stay quiet and let your parents deal with in case she gets mad.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to insult her so that she feels bad and leanrs from her mistake.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" take it upon yourself to positively teach her.")
                                        while not correct9:
                                            choice5 = input()
                                            if "1" in choice5:
                                                print (border)
                                                print ("You spooked her and she stopped coming to dinner.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to eat dinner when Mrs. Rogers is there.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to attend the dinner normally and be your playful self.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" attend the dinner but stay quiet and respectful, having less fun.")
                                            elif "2" in choice5:
                                                print (border)
                                                print ("Your parents politely explained to Mrs. Rogers why what she just said was wrong. You made a good choice, but not the best one.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to eat dinner when Mrs. Rogers is there.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to attend the dinner normally and be your playful self.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" attend the dinner but stay quiet and respectful, having less fun.")

                                            elif "3" in choice5:
                                                print (border)
                                                print ("She apologized to you and promised to be more careful in the future.\nSince, Mrs. Rogers has been warming up to you lately, there's no point in being a bystander!\nPolitely standing up for your culture was the right choice!\n\nType \"next\" to continue!")
                                                correct9 = True
                                                correct10 = False
                                                while not correct10:
                                                    choice6 = input()
                                                    if "n" in choice6.lower():
                                                        correct10 = True
                                                        print (border)
                                                        print ("You did it!")
                                                        print ("                                   Good job!")
                                                        print ("\n                                   .''.       ")
                                                        print ("         .''.      .      *''*    :_\/_:     . ")
                                                        print ("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
                                                        print ("  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
                                                        print (" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
                                                        print (" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
                                                        print ("  '..'  ':::'     * /\ *     .'/.\'.   '         ")
                                                        print ("      *            *..*         :                ")
                                                        print (termcolor.colored ("Thank you for playing Mrs. Roger's story! If you want to play Daniel's story restart the game!", 'red', attrs = ['bold']))
                                                
                                                    else:
                                                        print (border)
                                                        invalid(random.randint(1,3))
                                                
                                            else:
                                                print (border)
                                                invalid(random.randint(1,3))
                                    else:
                                        print (border)
                                        invalid(random.randint(1,3))
                                
                            else:
                                print (border)
                                invalid(random.randint(1,3))

    
                    
                   
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
        correct3 = True
        correct98 = False
        print ("It's your first day of school and you walk through the front doors!\nSuddenly, a tall boy says something mean about what you're wearing. What should you do?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ignore him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to comment on his ugly hair.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to tell a parent.")
        while not correct98:
            choice99 = input()
            if "1" in choice99:
                print (border)
                print ("You tried to ignore him but he followed you all the way to the classroom...\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ignore him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to comment on his ugly hair.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to tell a parent.")
            
            elif "3" in choice99:
                print (border)
                print ("You told your mom and she said she'd speak to the teacher.\nAlthough you don't need to tell everything to your parent, if someone is being mean they should be one of the first people you talk to.\n\nType \"next\" to continue!")
                correct98 = True
                correct97 = False
                while correct97 == False:
                    choice98 = input()
                    if "n" in choice98.lower():
                        correct97 = True
                        correct96 = False
                        print (border)
                        print ("Daniel has been mean to you ever since the first day of school. One day, you go to the bathroom and notice that he's locked outside of the \nschool. He looks kind of upset and it's pretty cold outside, should you still help him if he's really mean?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to go get a teacher to open the door for him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to try and pry open the door yourself.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to leave him oustide in the cold.")
                        while not correct96:
                            choice97 = input()
                            if "3" in choice97:
                                print (border)
                                print ("Leaving him outside made youf feel bad for the rest of the day. \n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to go get a teacher to open the door for him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to try and pry open the door yourself.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to leave him oustide in the cold.")                            
                            elif "2" in choice97:
                                print (border)
                                print ("You tried for 5 minutes but weren't strong enough to open the door. Daniel laughed at you.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to go get a teacher to open the door for him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to try and pry open the door yourself.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to leave him oustide in the cold.")
                            elif "1" in choice97:
                                print (border)
                                print ("A teacher came to let Daniel back in.\nYou chose the right option!\nAs long as you don't think they'll hurt you, you should always try to help people!\n\nType \"next\" to continue!")
                                correct96 = True
                                correct95 = False
                                while not correct95:
                                    choice96 = input()
                                    if "n" in choice96.lower():
                                        correct95 = True
                                        correct94 = False
                                        print (border)
                                        print ("Ever since you helped get the teacher to open the door, Daniel has been extra mean for some reason. One day you and him get lost on the \nsubway. You need to find the way home but bringing him with you might stop you from doing that. What should you do?\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to let him come with you.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" Tell him wrong directions and get him lost to get back at him.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" agree to walk together, even if he'll be really mean.")
                                        while not correct94:
                                            choice95 = input()
                                            if "1" in choice95:
                                                print (border)
                                                print ("What would your parents think if you left him!\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to let him come with you.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" Tell him wrong directions and get him lost to get back at him.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" agree to walk together, even if he'll be really mean.")
                                            elif "2" in choice95:
                                                print (border)
                                                print ("Even though he's mean to you doesn't mean you should put him in danger.\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to refuse to let him come with you.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" Tell him wrong directions and get him lost to get back at him.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" agree to walk together, even if he'll be really mean.")

                                            elif "3" in choice95:
                                                print (border)
                                                print ("You walked with him and he stayed surprisingly quiet.\nWhen people are lost and afraid, that's when they need help the most.\nType \"next\" to continue!")
                                                correct94 = True
                                                correct93 = False
                                                while not correct93:
                                                    choice94 = input()
                                                    if "n" in choice94.lower():
                                                        correct93 = True
                                                        print (border)
                                                        print ("You did it!")
                                                        print ("                                   Good job!")
                                                        print ("\n                                   .''.       ")
                                                        print ("         .''.      .      *''*    :_\/_:     . ")
                                                        print ("      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.")
                                                        print ("  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-")
                                                        print (" :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'")
                                                        print (" : /\ : :::::     *_\/_*     -= o =-  /)\    '  *")
                                                        print ("  '..'  ':::'     * /\ *     .'/.\'.   '         ")
                                                        print ("      *            *..*         :                ")
                                                        print (termcolor.colored ("Thank you for playing Daniel's story! If you want to play Mrs. Roger's story restart the game!", 'red', attrs = ['bold']))
                                                
                                                    else:
                                                        print (border)
                                                        invalid(random.randint(1,3))
                                                
                                            else:
                                                print (border)
                                                invalid(random.randint(1,3))
                                    else:
                                        print (border)
                                        invalid(random.randint(1,3))
                                
                            else:
                                print (border)
                                invalid(random.randint(1,3))

    
                    
                   
                    else: 
                        print (border)
                        invalid(random.randint(1,3))
            elif "2" in choice99:
                        print (border)
                        print ("Let's just pretend you didn't pick that...\n\nType \"", termcolor.colored ("1",'red',attrs = ['bold']), "\" to ignore him.\nType \"", termcolor.colored ("2",'red',attrs = ['bold']),"\" to comment on his ugly hair.\nType \"", termcolor.colored ("3",'red',attrs = ['bold']),"\" to tell a parent.")           
            else: 
                print (border)
                invalid(random.randint(1,3))
    



    else: 
        print (border)
        invalid(random.randint(1,3))





        


        





