n=int(input("N: "))
A1 = 1
A2 = 2
A3 = 3
for k in range(4,n+1):
    A4 = A3+A2-2*A1
    print(k," : ",A4)
    A1 = A2
    A2 = A3
    A3 = A4