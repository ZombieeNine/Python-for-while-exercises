k=float(input("Цена 1 кг конфет: "))
for i in range(1,11):
    x=i*0.1
    print("Стоимость ", x, 'кг:', (x*k))