
point = 0

def morning():
    actions = ["early", "ontime", "late"]
    global point
    temp = 0
    print("This is just another normal day for a Muslim. To start the day you decided to wakeup: ")
    userInput = ""
    while userInput not in actions:
        print("Options: early/ontime/late")
        userInput = input()
        if userInput == "early":
            goEarly(temp)
        elif userInput == "ontime":
            goOnTime(temp)
        elif userInput == "late":
            goLate()
        else:
            print("Invalid input. Please retype a valid option")

def Afternoon():
    print(point)
            
def goEarly(temp):
    actions = ["tahajjud", "sleep"]
    global point
    userInput = ""
    print("Great! You decided to wake up early. Do you want to "
                  + "perform tahajjud prayer? or do you want to go back to sleep ?")
    while userInput not in actions:
        print("Options: tahajjud/sleep")
        userInput = input()
        if userInput == "tahajjud":
            point += 1
            temp = 1
            goOnTime(temp)
        elif userInput == "sleep":
            goOnTime(temp)
        else:
            print("Invalid input. Please retype a valid option")

def goOnTime(temp):
    actions = ["subuh", "sleep"]
    global point
    userInput = ""
    if temp == 0:
        print("Good! You decided to wake up on time. Do you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?")
    else:
        print("Do you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?")
    while userInput not in actions:
        print("Options: subuh/sleep")
        userInput = input()
        if userInput == "subuh":
           Afternoon()
        elif userInput == "sleep":
            point -= 1
            goLate()
        else:
            print("Invalid input. Please retype a valid option")

def goLate():
    actions = ["yes", "no"]
    global point
    userInput = ""
    print("Astaghfirullahalazim... You woke up late and did not perform Subuh prayer. " +
          "Do you want to peform Qada' prayer ? ")
    while userInput not in actions:
        print("Options: yes/no")
        userInput = input()
        if userInput == "yes":
           Afternoon()
        elif userInput == "no":
            point -= 1
            Afternoon()
        else:
            print("Invalid input. Please retype a valid option")

morning()
