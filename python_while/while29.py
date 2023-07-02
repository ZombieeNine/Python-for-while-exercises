N=float(input("Number: "))
e=1/10**N
print("eps(N) = ",e)
A1=1
A2=2
A3=(A1+2*A2)/3
k=3
while abs(A3-A2)>=e:
    A2,A3=A3,(A2+2*A3)/3
    k+=1
    print(k,":",A3)
print()
print(f"K: {k}, A(K-1): {A2}, A(K): {A3}")
