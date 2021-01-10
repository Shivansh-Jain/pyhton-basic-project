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
