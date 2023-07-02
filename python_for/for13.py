n=int(input("Number: "))
c=0
for i in range(1,n+1):
    c+=((i/10)+1)*(pow(-1,i+1))
print("Result:",c)