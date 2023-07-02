import math
x=float(input("Number X: "))
n=int(input("Number N: "))
p = x
s = x
k = 1
for i in range(1,n+1):
    p*=k/((k+1)*(k+2))*x*x
    s+=p
    k+=2
    p*=k
print("Result: ",s,"\n","asin(x)=",math.asin(x))