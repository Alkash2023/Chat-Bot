school=[]
dnewnuk1={"имя":"Иван",
        "Матем":"5",
        "Биолог":"5",
        "Рус Яз":"5",
        "физ-ра":"5",
        "Изо":"5"}
dnewnuk2={"имя":"Олег",
        "Матем":"4",
        "Биолог":"4",
        "Рус Яз":"4",
        "физ-ра":"4",
        "Изо":"4"}
dnewnuk3={"имя":"Андрей",
        "Матем":"2",
        "Биолог":"2",
        "Рус Яз":"2",
        "физ-ра":"2",
        "Изо":"2"}
school.append(dnewnuk1)
school.append(dnewnuk2)
school.append(dnewnuk3)
w=(input("вас привествует Электронный дневник :введите найти ученика по имени/ узнать оценку"))
while w != "выход":
    if w == "найти ученика по имени":
        r=input("введите имя")
        for i in school:
            if i["имя"]==r:
                
                z=input("введите действие")
                if z =="изменить оценку":
                        name=(input("изменить по какому предмету? "))
                        print("ранее было:",i[name])
                        a=(input("введите новое значение: "))
                        i[name]=a
                        print(school)
                
                if z == "удалить оценку":
                        bame=(input("удалить что? "))
                        del i[bame]
                        print(school)
    if w =="узнать оценку":
        q=input("введите имя")
        if q=="Андрей":
            print(dnewnuk3)
        if q=="Олег":
            print(dnewnuk2)
        if q=="Иван":
            print(dnewnuk1)
    w=(input("впишите:найти ученика по имени/узнать оценку "))


