N=float(input("Number: "))
e=1/10**N
print("eps(N) = ",e)
A1=2
A2=2 + 1/A1
k=2
while abs(A2-A1)>=e:
    A1=A2
    A2=2+1/A2
    k+=1
    print(k,":",A2)
print()
print(f"K: {k}, A(K-1): {A1}, A(K): {A2}")