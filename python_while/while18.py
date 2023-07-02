N=int(input("N: "))
k=0
s=0
while N>=1:
    k+=1
    x=N%10
    s+=x
    N=int(N/10)
print("Кол-во цифр: ",k)
print("Сумма цифр: ",s)