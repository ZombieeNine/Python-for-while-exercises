a=int(input("A: "))
b=int(input("B: "))
c=1
for x in range(a,b+1):
    c*=x
print("Pow",c)