N=int(input("N: "))
F1=F2=1
i=2
while F2<N:
    F0,F1,F2=F1,F2,F1+F2
    i+=1
print()
print("Порядковый номер числа Фибоначчи: ",i)
