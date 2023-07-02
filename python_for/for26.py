import math
x=float(input("Number X: "))
n=int(input("Number N: "))
p = x
s = x
k = 1
for i in range(1,n+1):
    p *= -1*x*x
    k += 2
    s += p/k
print("Result: ",s,"\n","atan(x)=",math.atan(x))