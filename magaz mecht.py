magaz={"пить":"спрайт" "лимон+лайм","поедание": "пельмени-200""майонез-70","кайф":"комп""диван-1000"}
w=(input("вас привествует магазин с самыми большими ценами в городеи лучшими наборами"))
while w != "выход":
    if w=="ассортимент":
        print(magaz)
    if w=="покупка":
            a=(input("купить что? "))
            del magaz[a]
            print("осталось",magaz)
    if w=="возврат":
            e=(input("добавить что "))
            b=(input("введите предмет: "))
            magaz[e]=b
    w=(input("вас привествует магазин с самыми большими ценами в городе и лучшими н