n=[]
r=int(input("введите колво натуральных чисел  ")) 
for w in range(r):
    p=int(input("введите положительное число  "))
    n.append(p)
n.remove(max(n))
n.remove(min(n))
print(n)

