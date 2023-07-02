a=int(input("A:"))
b=int(input("B:"))
k=1
for i in range(a,b+1):
    for x in range(0,k):
        print(i,end=" ")
    print()
    k+=1