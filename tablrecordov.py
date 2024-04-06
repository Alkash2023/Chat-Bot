record=[]

w=(input("вас привествует таблица рекордов введите добавить новый рекорд или регистрация"))
while w != "выход":
    tabrecord={}
    
    rame=(input("введите имя "))
    b=(input("введите ""0"": "))
    tabrecord["имя"]=rame
    tabrecord["очки"]=b
    record.append(tabrecord)
    print(tabrecord)
        
    if w == "добавить новый рекорд":
        
        rame=(input("добавить по какому имени ? "))
        b=(input("введите значение: "))
        if record[-1]["очки"]<b:
            tabrecord["имя"]=rame
            tabrecord["очки"]=b
            record.append(tabrecord)
        print(record)
        
    w=(input("вас привествует таблица рекордов введите имя и рекорд "))
    
   
