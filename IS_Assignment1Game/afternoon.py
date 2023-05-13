import time

deed = 0

def mengumpat():
    actions = ["join", "walk away"]
    global deed
    
    print("[12:00PM]\nYou walk into the office and see your co-workers gossiping about the boss, what are you going to do?")
    userInput = ""
    
    while userInput not in actions:
        print("Options: join/walk away")
        userInput = input()
        if userInput == "join":
            print("\nYou joined the conversation that is useless and wasted your time.\n")
            deed-=1
            sleep()
            azan()
        elif userInput == "walk away":
            print("\nYou walked away from the conversation and spent your time doing your work.\n")
            deed+=1
            sleep()
            azan()
        else:
            print("Please enter a valid option.")

def azan(): 
    actions = ["continue", "respect"]
    global deed
    
    print("[1:12PM]\nYou were in the middle of presentating your monthly report to your boss when you heard the Zuhr call of prayer. Do you want to continue with the presentation or respect the call of prayer?")
    userInput = ""
    
    while userInput not in actions:
        print("Options: continue/respect")
        userInput = input()
        if userInput == "continue":
            print("\nYou continued with the presentation despite hearing the call of prayer.\n")
            deed-=0
            sleep()
            flirting()
        elif userInput == "respect":
            print("\nYou stop your presentation and informed your boss on the reason.\n")
            deed+=1
            sleep()
            flirting()
        else:
            print("Please enter a valid option.")

def flirting():
    actions = ["accept", "decline"]
    global deed
    
    print("[6:00PM]\nYou arrived home from work.\n\nWhile you were in the porch, your widowed neighbour next door greet you with a lustful intent.\n\nShe then invite you to come into her house, what's your decision?")
    userInput = ""
    
    while userInput not in actions:
        print("Options: accept/decline")
        userInput = input()
        if userInput == "accept":
            print("\nYou accepted her invitation and followed her into her house.\n")
            deed-=1
            sleep()
            goNight()
        elif userInput == "decline":
            print("\nYou politely decline her invitation and walk into your house.\n")
            deed+=0
            sleep()
            goNight()
        else:
            print("Please enter a valid option.")

def goNight():

    print("Your deed = " + str(deed))

    quit()

def sleep():
    time.sleep(1)

mengumpat()
