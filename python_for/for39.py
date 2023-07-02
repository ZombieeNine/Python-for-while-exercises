a=int(input("A:"))
b=int(input("B:"))

for i in range(a,b+1):
    for x in range(0,i):
        print(i,end=" ")
    print()