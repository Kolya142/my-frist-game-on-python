import time#
import os#
max = 10#max (the value, for edit)
nam = 0#nam (the value, not for edit)
def main(nam):#create "main(nam)"
    os.system("cls || clear")#clear
    x = 0#
    pr = "|"#start
    while x < nam:#x < nam
        pr += "*"#pr = (pr + "*")
        x += 1#
    pr += 'p'#create player
    x += 1#
    while x < max:#x < "max"
        pr += '*'#pr = (pr + "*")
        x += 1#
    pr += '|'#end
    print(pr)#show on console
os.system("cls || clear")#clear
print("\"p\" = player")#instructions
print("\"r\" = right")#instructions
print("\"l\" = left")#instructions
print("press (\"l\" and enter), for start")#
print("_____________")#instructions(end)
while 1==1:#infinity(while)
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
    else:#else (not if)
        print('error')#show on console "error"
        time.sleep(0.3)#timeout '0.3'
    main(nam)#main(nam) (start)