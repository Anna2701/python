revenue = int(input("Введите выручку фирмы "))
costs = int(input("Введите издержки фирмы "))
profit = revenue - costs
if profit:
    profitability = profit / revenue
    print(f"Прибыль = {profit}, рентабельность = {profitability}")
    workers = int(input("Введите количество сотрудников фирмы "))
    profit_workers = profit / workers
    print(f"Прибыль в расчете на одного сторудника сотавила = {profit_workers}")
else:
    print(f"Убыток = {profit}")
