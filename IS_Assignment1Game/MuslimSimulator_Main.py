

from tkinter import *
from tkinter import ttk

#Start of Tkinter windows
root = Tk()
root.geometry("460x600") #Size of Window
root.title("Muslim Simulator")

point = 0 # Player's final score

global fn # f(n) = h(n) + g(n) // path cost
fn = 0

global hn # Number of CHOICES made
hn = 0

global gn # Number of BAD CHOICES made
gn = 0

#Frame per main scenes (3 main scenes)
morningScene = Frame(root, padx=5, pady=5)
morningScene.grid(row=1, columnspan=3, sticky="NW")

afternoonScene = Frame(root, padx=5, pady=5)
afternoonScene.grid(row=1, columnspan=4, sticky="NW")

nightScene = Frame(root, padx=5, pady=5)
nightScene.grid(row=1, columnspan=4, sticky="NW")

#Main scene 1 (Intro & Morning)

#Introduction function [Start of Window]
def intro():
    global point
    point = 0

    #widgets
    greet = Label(morningScene, text="Welcome to Muslim Simulator 2023!")
    introduction = Label(morningScene, text="In this journey, we will decide whether you're a good Muslim or otherwise." +
                         "\n Be aware that all your choices are meaningful and will decide your fate!", justify=CENTER)

    #Display of Widgets
    greet.grid(column=1,row=0)
    introduction.grid(columnspan=3, row=1)

#Morning Function [First sub-scene in Morning scene]
def morning():
    temp = 0

    #widgets
    morningGreet = Label(morningScene, text="\nThis is just another normal day for a Muslim. To start the day you decided to wakeup: \n")
    early = Button(morningScene, text="Early", padx=20, pady=10, command=lambda: goEarly(temp))
    onTime = Button(morningScene, text="On Time", padx=20, pady=10, command=lambda: goOnTime(temp))
    late = Button(morningScene, text="Late", padx=20, pady=10, command=lambda: goLate())

    #Display of Widgets
    morningGreet.grid(columnspan=3, row=2)
    early.grid(column=0,row=3)
    onTime.grid(column=1, row=3)
    late.grid(column=2, row=3)

#goEarly Function [Choosing of Tahajjud or not]
def goEarly(temp):
    global hn

    #widgets
    earlyGreet = Label(morningScene ,text="\n\n[4:30 AM]\nGreat! You decided to wake up early.\nDo you want to "
                  + "perform tahajjud prayer ? or do you want to go back to sleep ?\n")
    tahajjud = Button(morningScene, text="Tahajjud", padx=20, pady=10, command=lambda: goTahajjud(temp))
    sleep = Button(morningScene, text="Sleep", padx=20, pady=10, command=lambda: goOnTime(temp))

    #Display of Widgets
    earlyGreet.grid(columnspan=3, row=4)
    tahajjud.grid(column=0, columnspan=2, row=5)
    sleep.grid(column=1, columnspan=2, row=5)

    hn += 1

#goTahajjud Function [To record the points of choosing in goEarly]
def goTahajjud(temp):
    global point
    point += 1
    temp = 1
    goOnTime(temp)

#goOnTime Function [Choosing of Subuh or not]
def goOnTime(temp):
    global hn

    #widgets
    if temp == 0:
        onTimeGreet = Label(morningScene, text="\n\n[6:00 AM]\nGood! You decided to wake up on time. \nDo you want to perform Subuh" +
                  " prayer ? or do you want to go back to sleep ?\n")
    
    else:
        onTimeGreet = Label(morningScene, text="\n\n[6:00 AM]\nGood! Do you want to perform Subuh" +
                  " prayer ?\nor do you want to go back to sleep ?\n")
    
    subuh = Button(morningScene, text="Subuh", padx=20, pady=10, command=lambda: goAfternoon())
    sleep = Button(morningScene, text="Sleep", padx=20, pady=10, command=lambda: goSleep())

    #Display of Widgets
    onTimeGreet.grid(columnspan=3, row=6)
    subuh.grid(column=0, columnspan=2, row=7)
    sleep.grid(column=1, columnspan=2, row=7)

    hn += 1

#goSleep Function [To record the points of choosing in goOnTime]
def goSleep():
    global point
    point -= 1
    goLate()


#goLate Function [Choosing of Qada' or not (if Subuh was not done)]
def goLate():
    global hn
    global gn

    #widgets
    lateGreet = Label(morningScene, text="\n\n[7:30 AM]\nAstaghfirullahalazim... You woke up late and did not perform Subuh prayer." +
          "\nDo you want to peform Qada' prayer ?\n")
    yesQada = Button(morningScene, text="Yes", padx=20, pady=10, command=lambda: goQada(1))
    noQada = Button(morningScene, text="No", padx=20, pady=10, command=lambda: goQada(2))

    #Display of Widgets
    lateGreet.grid(columnspan=3, row=8)
    yesQada.grid(column=0, columnspan=2, row=9)
    noQada.grid(column=1, columnspan=2, row=9)

    hn += 1
    gn += 1


#goQada Function [To record the points of choosing in goLate]
def goQada(qada):
    global point
    global gn 

    if qada == 1:
        point += 1
        goAfternoon()

    else:
        point -= 1
        gn += 1
        goAfternoon()


#Main Scene 2 (Afternoon Scene)

#goAfternoon Function [Switch of Frame and start of first night sub-Scene]
def goAfternoon():
    global hn

    #widgets
    morningScene.destroy()
    afternoonGreet = Label(afternoonScene, text="\n[12:00 PM]\nYou walk into the office and see your co-workers gossiping about the boss." +
                           "\n\tWhat are you going to do?\n")
    yesRant = Button(afternoonScene, text = "Join", padx=20, pady=10, command=lambda: goRant(1))
    noRant = Button(afternoonScene, text = "Walk\nAway", padx=20, pady=3, command=lambda: goRant(2))

    #Display of Widgets
    afternoonGreet.grid(columnspan=3, row=10)
    yesRant.grid(column=0, columnspan=2, row=11)
    noRant.grid(column=1, columnspan=2, row=11)

    hn += 1

#goRant Function [To record the points of choosing in goAfternoon]
def goRant(rant):
    global point
    global gn
    
    if rant == 1:
        point -= 1
        gn += 1
        goAzan()
    
    else:
        point += 1
        goAzan()

#goAzan Function [Choosing of respecting Adzan or not]
def goAzan():
    global hn

    #widgets
    azanGreet = Label(afternoonScene, text="\n\n[1:12 PM]\nYou were in the middle of presentating your monthly report to your boss." +
                      "\nThen you heard the Zuhr call of prayer (Adzan)." +
                      "\nDo you want to continue with the presentation or respect the call of prayer?\n")
    noRespect = Button(afternoonScene, text="Continue\nMeeting", padx=20, pady=10, command=lambda: goRespect())
    respect = Button(afternoonScene, text="Respect\nAdzan", padx=20, pady=10, command=lambda: goRespect())

    #Display of Widgets
    azanGreet.grid(columnspan=3, row=12)
    noRespect.grid(column=0,columnspan=2, row=13)
    respect.grid(column=1, columnspan=2, row=13)

    hn += 1

#goRespect Function [To record the points of choosing in goAzan]
def goRespect():
    global point
    global hn

    point += 1
    hn += 1
    goNight()


#Main Scene 3 (Night Scene)

#goNight Function [Switch of Frame and start of first night sub-Scene]
def goNight():
    global hn

    #widgets
    afternoonScene.destroy()
    nightGreet = Label(nightScene, text="\n\n[7:00 PM]\nIt is the end of the day, you are tired but still have obligations as a Muslim." +
                       "\nFor Maghrib, will you be going to the mosque?\n")
    prayMosque = Button(nightScene, text="Pray at\nMosque", padx=20, pady=10, command=lambda: goMosque(1))
    prayHome = Button(nightScene, text="Pray at\nHome", padx=20, pady=10, command=lambda: goMosque(2))

    #Display of Widgets
    nightGreet.grid(columnspan=3, row=14)
    prayMosque.grid(column=0, columnspan=2, row=15)
    prayHome.grid(column=1, columnspan=2, row=15)

    hn += 1

#goMosque Function [To record the points of choosing in goNight]
def goMosque(mosque):
    global point

    if mosque == 1:
        point += 1
        stayMosque()

    else:
        point -= 0
        endScene()

#stayMosque Function [Choosing of staying in Mosque or not]
def stayMosque():
    global hn

    #widgets
    mosqueGreet = Label(nightScene, text="\n\n[8:00 PM]\nIt is not long until Isya'\nWill you go back home or stay to pray?\n")
    stayMosque = Button(nightScene, text="Stay at\nMosque", padx=20, pady=3, command=lambda: goIsya(1))
    goHome = Button(nightScene, text="Go Home", padx=20, pady=10, command=lambda: goIsya(2))

    #Display of Widgets
    mosqueGreet.grid(columnspan=3, row=16)
    stayMosque.grid(column=0, columnspan=2, row=17)
    goHome.grid(column=1, columnspan=2, row=17)

    hn += 1

#goIsya Function [To record the points of choosing in statMosque]
def goIsya(Isya):
    global point

    if Isya == 1:
        point += 1
        endScene()

    else:
        point -= 0
        endScene()


#endScene Function [Function to use A* Search to calculate path]
def endScene():
    global point
    global hn
    global fn

    fn = gn + hn # final path cost
    
    #widgets
    if point >= 0: #if points accumulated is positive, we labeled as good Muslim
        endGreet = Label(nightScene, text="\n\nYou have ended your day!\nTotal point(s) is: " + str(point) +
                         "\nYou are on the right path towards Rahmatan Lil Alamin!\n" + "\nNumber of bad choices made = " + str(gn) + "\n" + "Number of choices made = " + str(hn) + "\n" +  "Total path = " + str(fn))

    else: #if points accumulated is negative, we labeled as bad Muslim
        endGreet = Label(nightScene, text="\n\nYou have ended your day!\nTotal point(s) is: " + str(point) +
                         "\nAllah SWT still loves you. InsyaAllah, you will return to the right path\n" + "\nNumber of bad choices made = " + str(gn) + "\n" + "Number of choices made = " + str(hn) + "\n" +  "Total path = " + str(fn))
        
    if fn == 5: #5 is the optimal path in our text-based adventure game
        conclusion = Label(nightScene, text="\nCongratulations! You have chosen the most optimal path")
    
    else: #more than 5, we will notify the user.
        conclusion = Label(nightScene, text="\nYou could have chosen a more optimal path.")

    #Display of Widgets
    endGreet.grid(columnspan=3, row=20)
    conclusion.grid(columnspan=3, row = 25)

intro()
morning()

root.mainloop()