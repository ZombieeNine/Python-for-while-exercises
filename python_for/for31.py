n=int(input("N: "))
A0 = 2
for k in range(1,n+1):
    A1 = 2 + 1/A0
    print(k," : ",A1)
    A0 = A1