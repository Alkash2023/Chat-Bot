import mylib
# массивы и функция vyvodPolya в файле mylib.py           

mylib.vyvodPolya(mylib.vidimost_polya)
game = True
def f (pole):
    if pole == "✴":
        return False
    else:
        return True
while game:
    stroka = int(input("Введите номер строки"))
    stolb = int(input("Введите номер столбца"))
    if stroka >12:
        print("невозможная координата ")
    elif stolb >12:
        print("невозможная координата ")
    elif stroka <0 or stolb <0 :
        print("невозможная координата ")
    else:
        mylib.check(stroka-1,stolb-1)
        mylib.vyvodPolya(mylib.vidimost_polya)
    if mylib.isOpen():
        game = False
    if f(mylib.pole[stroka][stolb])==False:
        print("вы проиграли")
print("Всё поле открыто!")

