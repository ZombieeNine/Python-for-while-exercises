b =float(input("B: "))
a =float(input("A: "))
n =int(input("N: "))
h = (b - a) / n
print("H = ",h)
x = a
for i in range(0,n):
    print(x,end=", ")
    x += h
print(x)