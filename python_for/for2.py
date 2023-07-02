a=int(input("A: "))
b=int(input("B: "))
c=0
if a<b:
    for n in range(a,b+1):
        print(n)
        c+=1
    print("Количество N чисел",c)
else:
    print("Error")
    


# i=1
# c=[]
# for i in range(2,100,2):
#     c.append(i)
# print(c)