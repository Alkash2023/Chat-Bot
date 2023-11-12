asdghjm=[["8","8","8"],
         ["8","8","8"],
         ["8","8","8"]]
x=int(input("введите X для x "))
x1=int(input("введите Y для x "))
y=int(input("введите X для y "))
y1=int(input("введите Y для y "))
while 1:
    asdghjm[x][x1]="x"
    asdghjm[y][y1]="o"
    for i in asdghjm:
        print(i)
    x=int(input("введите X для x "))
    x1=int(input("введите Y для x "))
    y=int(input("введите X для y "))
    y1=int(input("введите Y для y "))
