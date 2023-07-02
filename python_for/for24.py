import math
x=float(input("Number X: "))
n=int(input("Number N: "))
f=1
s=1
k=1
for i in range(1,n+1):
    f*=(-1)*x*x/(k*(k+1))
    s+=f
    k+=2
print("Result: ",s,"\n",f"cos({x})=",math.cos(x))