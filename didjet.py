import random as r

pole = [["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"],
        ["*","*","*","*","*","*","*","*","*","*","*","*"]]

vidimost_polya=[["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"],
                ["•","•","•","•","•","•","•","•","•","•","•","•"]]
# ✴
#
for i in range(3):
    rag=r.randint(0,len(pole)-1)
    rak=r.randint(0,len(pole[0])-1)
    pole[rag][rak]="✴"

def vyvodPolya(spisok):
    for stroka in spisok:
        for kletka in stroka:
            print(kletka,end='')
        print()


def check(stroka,stolb):
    if vidimost_polya[stroka][stolb] == "•":
        vidimost_polya[stroka][stolb] = pole[stroka][stolb]
        if pole[stroka][stolb] == "*":
            if stroka-1 >= 0:
                check(stroka-1,stolb)
                if stolb-1 >= 0:
                    check(stroka-1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka-1,stolb+1)
                    
            if stroka+1 < len(pole):
                check(stroka+1,stolb)
                if stolb-1 >= 0:
                    check(stroka+1,stolb-1)
                if stolb+1 < len(pole[stroka]):
                    check(stroka+1,stolb+1)
                    
            if stolb-1 >= 0:
                    check(stroka,stolb-1)
            if stolb+1 < len(pole[stroka]):
                check(stroka,stolb+1)
def isOpen():
    opened = True
    all_bombs = 0
    for stroka in range (len(pole)):
        if "•" in vidimost_polya[stroka]:
            opened = False
        else:
            for stolb in range (len(pole[stroka])):
                if vidimost_polya[stroka][stolb]=="📍" and pole[stroka][stolb]=="✴":
                    all_bombs += 1
    return opened and (all_bombs == 3)
def didjet(pole):
    for stroka in range (len(pole)):
        for stolb in range (len(pole[stroka])): 
            bomb=0
            if pole[stroka][stolb]!="✴":
                    
                if stroka-1 >= 0:
                    if pole[stroka-1][stolb]=="✴":
                        bomb=bomb+1
                    if stolb-1 >= 0:
                        if pole[stroka-1][stolb-1]=="✴":
                            bomb=bomb+1
                    if stolb+1 < len(pole[stroka]):
                        if pole[stroka-1][stolb+1]=="✴":
                            bomb=bomb+1
                if stroka+1 < len(pole):
                    if pole[stroka+1][stolb]=="✴":
                            bomb=bomb+1
                    if stolb-1 >= 0:
                        if pole[stroka+1][stolb-1]=="✴":
                            bomb=bomb+1
                    if stolb+1 < len(pole[stroka]):
                        if pole[stroka+1][stolb+1]=="✴":
                            bomb=bomb+1
                if stolb-1 >= 0:
                    if pole[stroka][stolb-1]=="✴":
                        bomb=bomb+1
                if stolb+1 < len(pole[stroka]):
                    if pole[stroka][stolb+1]=="✴":
                        bomb=bomb+1
                if bomb >= 1:
                    pole[stroka][stolb]=str(bomb)
                
        
didjet(pole)

