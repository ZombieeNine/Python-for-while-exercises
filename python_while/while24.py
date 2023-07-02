N=int(input("N: "))
F1=F2=1
while F2<N:
    F1,F2=F2,F1+F2
if F2 == N:
    print("TRUE")
else:
    print("FALSE")