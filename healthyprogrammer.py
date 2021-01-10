#This is a program for a person who sits in front of a computer for hours, this program assumes that you work continuously from 9 am to 6 pm, this program is like a reminder program which reminds to drink water every 10 minutes (assuring that you drink approx. 3.5 liter of water during your working hours), it reminds you to relax your eye every 30 min (for better eye health), it also reminds you to do some physical activity every 45 minutes (so that you feel fresh every time), this program also keeps a record of your responses after every task so that you can evaluate them later. Before starting the program ask you whether you want to start it or not once started the program will automatically ends at 6 pm. 
#note= If you want to run the program kindly change the music file path.
 

import pygame

def water():
    import datetime
    pygame.init()
    load = ("G:\download\It's time to drink water sound.mp3")
    pygame.mixer.music.load(load)

    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    decision = input("Did you Drink water? (Y or N) ").upper()
    if decision not in ['Y','N']:
        print("Please give a valid input: ")
        decision = input("Did you Drink water? (Y or N) ").upper()
    elif decision=='Y':
        with open("waterchart.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Done'+'\n')
    elif decision =="N":
        with open("waterchart.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Ignored'+'\n')


    play=True
    while play:
        if decision in ["Y","N"]:
            pygame.mixer.music.stop()
            play=False

def eye():
    import datetime
    pygame.init()
    load = ("H:\music\gta_ringtone.mp3")
    pygame.mixer.music.load(load)

    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    decision = input("Do you fill relaxed now? (Y or N) ").upper()
    if decision not in ['Y','N']:
        print("Please give a valid input: ")
        decision  = input("Do you fill relaxed now? (Y or N) ").upper()
    elif decision=='Y':
        with open("relax.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Done'+'\n')
    elif decision =="N":
        with open("relax.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Ignored'+'\n')


    play=True
    while play:
        if decision in["Y","N"]:
            pygame.mixer.music.stop()
            play=False


def activity():
    import datetime
    pygame.init()
    load = ("H:\music\Dum Dee Dum - 320 Kbps - DownloadMing.SE.mp3")
    pygame.mixer.music.load(load)

    # pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()
    decision = input("Have you done some physical activity (Y or N) ").upper()
    if decision not in ['Y','N']:
        print("Please give a valid input: ")
        decision = input("Have you done some physical activity (Y or N) ").upper()
    elif decision=='Y':
        with open("activity.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Done'+'\n')

    elif decision =="N":
        with open("activity.txt",'a') as f:
            f.write(': '+str(datetime.datetime.now())+' - '+'Ignored'+'\n')
    play=True
    while play:
        if decision in ["Y","N"]:
            pygame.mixer.music.stop()
            play=False


def healthyprogrammer():
    import datetime, schedule
    start=input("Do you want to start the programme (Y,N)? ").upper()
    if start=="Y":
        schedule.every(10).minutes.do(water)
        schedule.every(30).minutes.do(eye)
        schedule.every(45).minutes.do(activity)

        while str(datetime.datetime.now().strftime("%H:%M:%S"))<str(datetime.time(18,31,00)):
            schedule.run_pending()

healthyprogrammer()
