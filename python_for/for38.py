n=int(input("N: "))
s = 0
for i in range(1,n+1):
    p=1
    k = n+1-i
    for j in range(0,k):
        p*=i
    s += p
print("Sum = ",s)