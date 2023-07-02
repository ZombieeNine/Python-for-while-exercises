n=int(input("N: "))
A0 = 1
for k in range(1,n+1):
    A1 = (A0+1)/k
    print(k," : ",A1)
    A0 = A1