import math
x=float(input("Number X: "))
n=int(input("Number N: "))
f=1
s=1
for i in range(1,n+1):
    f*=x/i
    s+=f
print("Result: ",s,"\n","e=",math.exp(x))
