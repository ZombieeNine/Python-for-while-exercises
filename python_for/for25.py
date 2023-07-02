import math
x=float(input("Number X: "))
n=int(input("Number N: "))
f = 1
s = 0
for i in range(1,n+1):
    f *= x
    s += f/i
    f *= -1
print("Result: ",s,"\n","ln(1+x)=",math.log(x+1))