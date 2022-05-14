#Made by Kolya142
import keyboard#
import random#
import time#
import os#
print("start")
max = 90#max (the value, for edit)
timeout = 0.01
start = 1#start (the value, not for edit)
namy = 1#nam (the value, not for edit)
nam = 0#nam (the value, not for edit)
print("max = " + str(max))
while nam < namy:
    while nam - namy < 10:
        namy = random.randrange(2,(max - 1))#nam (the value, not for edit)
        nam = random.randrange(1,(max - 1))#nam (the value, not for edit)
os.system("cls || clear")#clear
bonus = "b"#bunus (the value, for edit)
player = "p"#player (the value, for edit)
def bot():
    global timeout
    global namy
    global nam
    time.sleep(timeout)
    ran = random.randrange(0,6)
    ran1 = random.randrange(0,20)
    if ran1 < 2:
        if nam - namy < 2:
            os.system("cls || clear")#clear
            print("bot win")
            time.sleep(0.6)#timeout '0.6'
            exit() 
    elif ran < 4:
        if namy + 2 == nam:
            ran = random.randrange(0,8)
            if ran < 2:
                namy -= 2
        if not namy - 1 == max:
            if not namy + 1 == nam:
                namy += 1
            else:
                ran = random.randrange(0,6)
                if ran < 3:
                    namy -= 1
                namy += 2
    else:
        if not namy == 1:
            namy -= 1
def main(nam):#create "main(nam)"
    line = "|"
    y = 0
    while y < ((nam / 2) - 5):
        line += "."
        y += 1
    y += 1
    line += str((nam + 1))
    while y < 10 :
        line += '*'
        y += 1
    line += player + '|' + bonus
    y = 0
    while y < ((nam / 2) - 5):
        line += "."
        y += 1
    y += 1
    line += str(nam - namy)
    while y < 10 :
        line += '*'
        y += 1
    line += player + '|'
    os.system("cls || clear")#clear
    #...................................
    print(line)
    x = 0#
    pr = "|"#start
    while x < namy:#x < namy
        pr += "."#pr = (pr + "*")
        x += 1#
    pr += bonus
    while x < nam:#x < nam
        pr += "~"#pr = (pr + "*")
        x += 1#    
    pr += player#create player
    x += 1#
    while x < max:#x < "max"
        pr += '*'#pr = (pr + "*")
        x += 1#
    pr += ('|')#end
    if nam == (namy - 1):
        os.system("cls || clear")#clear
        print("your win")
        time.sleep(0.6)#timeout '0.6'
        exit()
    elif nam < namy:
        os.system("cls || clear")#clear
        print("bot win")
        time.sleep(0.6)#timeout '0.6'
        exit()
    else:
        print(pr)#show on console
        print("___________________________________________________")
time.sleep(0.02)
os.system("cls || clear")#clear
print('"' + player+ '"' + " = player")#instructions
print("\"r\" = right")#instructions
print("\"l\" = left")#instructions
print("\"e\" = fire")#instructions
print("\"end\" = exit")#instructions
print('"' + bonus+ '"' + " = bot")#instructions
print("press \"enter\", for start")#
print("_____________")#instructions(end)
input()
while 1==1:#infinity(while)
    bot() #<-- the command, for import bot 
    if keyboard.is_pressed('r'):#if
        if not nam > (max - 2):#if
            nam += 1
        else:#else (not if)
            nam = (max - 1)
    elif keyboard.is_pressed('l'):#elif
        if not nam < 1:#if
            nam -= 1
        else:#else (not if)
            nam = 0
    elif keyboard.is_pressed('e'):#elif
        ran = random.randrange(0,6)
        if ran < 4:
            if nam - namy < 10:
                player = ("<<<<<<<<<<< " + player)
                nam = namy
                time.sleep(0.02)
                timeout = 0.001
    #elif o == 'end':#exit
        #os.system("cls || clear")#clear
        #break#exit
    elif keyboard.is_pressed('s'):#start
        main(nam)#main(nam) (start)
    main(nam)#main(nam) (start)