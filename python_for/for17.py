a=float(input("Число: "))
n=int(input("Степень: "))
c = 1.0
s = 1.0
for i in range(1,n+1):
    c *= a
    s += c
    # print("Sum",s)
print("Result:",s)