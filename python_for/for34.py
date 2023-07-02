n=int(input("N: "))
A1 = 1
A2 = 2
for k in range(3,n+1):
    A3 = (A1 + 2*A2)/3
    print(k," : ",A3)
    A1 = A2
    A2 = A3