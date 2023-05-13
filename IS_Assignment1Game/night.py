point = 0
def night():
    actions = ["pray at mosque", "pray at house"]
    global point
    print("It is the end of the day, you are tired but still have obligations as a muslim")
    userInput = ""
    while userInput not in actions:
        print("Options: pray at mosque/pray at house")
        userInput = input()
        if userInput == "pray at mosque":
            print("OTW to mosque for Maghrib prayer")
            point += 1
            mosque()
        elif userInput == "pray at house":
            print("getting ready for Maghrib prayer")
            point += 1
            house()

def mosque():
    actions = ["stay at mosque", "go home"]
    global point
    print("What will you do in between maghrib and isyak time")
    userInput = ""
    while userInput not in actions:
        print("Options: stay at mosque/go home")
        userInput = input()
        if userInput == "stay at mosque":
            print("You decided to do religious activities and pray isyak")
            point += 1
            athome()
        elif userInput == "go home":
            print("You decided to go home")
            point += 1
            athome()

def athome():
    actions = ["sleep", "watch movies", "pray isyak"]
    global point 
    print("What should you do after maghrib prayer ?")
    userInput = ""
    while userInput not in actions:
        print("Options: sleep/watch movies/pray isyak (if you not done yet)")
        userInput = input()
        if userInput == "sleep":
            print("You wake up to perform muslims obligations")
            point += 1
        elif userInput == "watch movies":
            print("You woke up late and missed subuh prayer!!")
            point += 0
        elif userInput == "pray isyak":
            print("You still have time, what u want to do")
            point += 1
            athome()
        
def house():
    actions = ["read quran", "eat"]
    global point 
    print("what shud u do after maghrib prayer ?")
    userInput = ""
    while userInput not in actions:
        print("Options: read quran/eat")
        userInput = input()
        if userInput == "read quran":
            print("sadaqallahul azim")
            point += 1
            athome()
        elif userInput == "eat":
            print("Alhamdulillah")
            point += 1
            athome()

night()
print(point)

#9/5/2023