#Made by Kolya142
import random#
import time#
import os#
print("start")
max = 40#max (the value, for edit)
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
    global namy
    ran = random.randrange(0,6)
    if ran < 3:
        if not namy - 1 == max:
            if not namy + 1 == nam:
                namy += 1
            else:
                ran = random.randrange(0,6)
                if ran < 3:
                    namy -= 1
    else:
        if not namy == 0:
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
    line += '|' + bonus
    y = 0
    while y < ((nam / 2) - 5):
        line += "."
        y += 1
    y += 1
    line += str(nam - (namy - 1))
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
        input("")
        exit()
    else:
        print(pr)#show on console
os.system("cls || clear")#clear
print('"' + player+ '"' + " = player")#instructions
print("\"r\" = right")#instructions
print("\"l\" = left")#instructions
print("\"end\" = exit")#instructions
print('"' + bonus+ '"' + " = bot")#instructions
print("press (\"s\" and enter), for start")#
print("_____________")#instructions(end)
while 1==1:#infinity(while)
    bot() #<-- the command, for import bot 
    o = input("")#input(༼ つ ◕_◕ ༽つ)
    if o == 'r':#if
        if not nam > (max - 2):#if
            nam += 1
        else:#else (not if)
            nam = (max - 1)
    elif o == 'l':#elif
        if not nam < 1:#if
            nam -= 1
        else:#else (not if)
            nam = 0
    elif o == 'end':#exit
        os.system("cls || clear")#clear
        break#exit
    elif o == 's':#start
        main(nam)#main(nam) (start)
    else:#else (not if)
        print('error')#show on console "error"
        time.sleep(0.3)#timeout '0.3'
    main(nam)#main(nam) (start)