a=float(input("Число: "))
n=int(input("Степень: "))
x=1
for i in range(1,n+1):
    x*=a
    print(a," в степени ", i," равно",x)