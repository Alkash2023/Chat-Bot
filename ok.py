import random as w
def y():
    s=w.randint(100,999)
    return s    
r=y()
def cheek(a,b):
    if a==b:
        print("молодец правильно ")
        return 1
    elif str(a)[0]==str(b)[0] or str(a)[1]==str(b)[1]:
        print("Горячо. ")
    elif str(b)[0] in str(a) or str(b)[1] in str (a) or str(b)[2] in str (a):
        print("тепло")
    else: print("холодно.")
i=int(input("введите число "))
print (r)
while 1:
    cheek(r,i)
    i=int(input("введите число"))
    
