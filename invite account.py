chat=[]

w=(input("вас привествует бот введите информацию о аккаунте"))
while w != "выход":
    if w == "вход":
        name=(input("введите логин по которому входите "))
        a=(input("введите пароль "))
        for item in chat:
            if name in item.keys():
                if item[name]==a:
                    print("вы вошли")
        
    if w == "регистрация":
        log=("введите логин если такой логин уже есть то аккаунт несоздатся ")
        lame=(input("введите логин"))
#         if lame ==chat{}
#             print("отказ в регистрации")
        rame=(input("введите пароль "))
        eame=(input("повторите пароль"))
        if rame != eame:
            print("отказ в регистрации")
        else:
            chat.append({lame:rame})
        print(chat)
        
    w=(input("вас приветствует бот введите информацию о аккаунте "))
