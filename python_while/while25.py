N=int(input("N: "))
F1=F2=1
while F2<=N:
    F1,F2=F2,F1+F2
print(F2)