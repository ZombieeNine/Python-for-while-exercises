a=int(input("A: "))
b=int(input("B: "))
c=0
for x in range(a,b+1):
    c+=x*x
print("Sum of squares",c)