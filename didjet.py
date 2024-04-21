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
