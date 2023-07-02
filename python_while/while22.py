N=int(input("N: "))
i=2
c=True
while i*i<=N:
    if N%i==0:
        c=False
        break
    i+=1
print(c)