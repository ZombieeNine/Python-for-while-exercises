import math
x=float(input("Number X: "))
n=int(input("Number N: "))
p=x/2
s=1 + x/2
k=2
for i in range(2,n+1):
    k+=2
    p*=(-1)*(k-3)/k * x
    s+=p
print("Result: ",s,"\n","sqrt(1+x)=",math.sqrt(1+x))