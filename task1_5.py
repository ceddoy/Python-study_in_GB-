print('Ваша фирма ООО "Рога и копыта", запрос по текущему месяцу')
revenue = int(input("Сколько составила выручка (руб.): "))
expenses = int(input("Сколько составило расходов (руб.): "))
profit = revenue - expenses
if profit > 0:
    print(f"Ваша фирма имеет прибыль в этом месяце: {profit} руб.")
    staff_firm = int(input("Сколько сотрудников работает в вашем Обществе: "))
    profit_staff = profit / staff_firm
    print(f"Финансовый результат, полученный одним работником составляет: {profit_staff:.2f} руб.")
elif profit < 0:
    print(f"Ваша фирма несет убытки в этом месяце: {profit}")
else:
    print("Ваша фирма имеет нулевой баланс")
