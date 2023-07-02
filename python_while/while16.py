P=float(input("Процент длины пробега: "))
if P>50 or P<0: 
    print("ERROR") 
    exit()
S1=10
S2=200
K=1
while S1<S2:
    S1*=1+P/100
    K+=1
    print(f"K = {K}, S = {S1} ")
print()
print(f"Кол-во дней = {K}, Сумарный пробег = {S1}")