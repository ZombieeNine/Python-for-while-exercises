n=int(input("N: "))
k=int(input("K: "))
s = 0
for i in range(1,n+1):
    p = 1.0
    for j in range(1,k+1):
        p *= i
    s += p

print("Sum = ",s)