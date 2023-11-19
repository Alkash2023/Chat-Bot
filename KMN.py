from random import randint
w=['камень','ножницы','бумага']
r=randint(0,2)
print("давай сыграем в камень ножницы бумага")
q=(input("введите свой ответ "))
print(w[r])
if q=="ножницы":
    if r == 2:
        print("победа")
    elif r==1:
        print("поражение")
    else:print("ничья")
elif q=="камень":
    if r == 1:
        print("победа")
    elif r==2:
        print("поражение")
    else:print("ничья")
elif q=="бумага":
    if r == 0:
        print("победа")
    elif r==1:
        print("поражение")
    else:print("ничья")
