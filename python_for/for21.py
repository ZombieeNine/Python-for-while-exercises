import math
n=int(input("Number: "))
f=1
s=1
for i in range(1,n+1):
    f/=i
    s+=f
print("Result: ",s,"\n","e=",math.exp(1))
