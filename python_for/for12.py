n=int(input("Number: "))
c=1
for i in range(1,n+1):
    x=1+i*0.1
    c*=x
print("Pow: ",c)