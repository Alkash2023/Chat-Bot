s=int(input("введите корд x "))
w=int(input("введите корд y "))
def draw_box(g,a):
    for i in range(1):
        print("*"*g)
    for i in range(a-2):
        print("*"," "*(g-4),"*")
    for i in range(1):
        print("*"*g)
draw_box(s,w)
draw_box
