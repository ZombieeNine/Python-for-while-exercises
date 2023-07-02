import math

b =float(input("B: "))
a =float(input("A: "))
n =int(input("N: "))
h = (b - a) / n
print("H = ",h)

x = a
for i in range(0,n+1):
    y = 1 - math.sin(x)
    print(f"{x} : {y}")
    x += h