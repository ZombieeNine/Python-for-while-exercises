n=int(input("N: "))
F1=1
F2=1
for k in range(3,n+1):
    F3 = F1 + F2
    print(k," : ",F3)
    F1 = F2
    F2 = F3