a=int(input("A: "))
b=int(input("B: "))
c=0
if a<b:
    for n in range(b-1,a,-1):
        print(n)
        c+=1
    print("Количество N чисел",c)
else:
    print("Error")
    