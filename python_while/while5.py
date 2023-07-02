k=int(input("enter N: "))
n=2**k
print('N = ', n)
x=0
while n>=2:
    n/=2
    x+=1
print("K: ",x)
