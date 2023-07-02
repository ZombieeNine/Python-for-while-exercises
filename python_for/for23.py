import math
x=float(input("Number X: "))
n=int(input("Number N: "))
f=x
s=x
k=0
for i in range(1,n+1):
    k+=2
    f*=(-1)*x*x/(k*(k+1))
    s+=f
print("Result: ",s,"\n",f"sin({x})=",math.sin(x))

