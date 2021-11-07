income = int(input("Введите сумму выручки: "))
expence = int(input("Введите сумму расходов: "))

profit = income - expence
if profit < 0:
    comment = 'Отрицательный, убыток'
elif profit == 0:
    comment = 'Сработаль в ноль, доход'
else:
    comment = 'Положительный, доход'
print(f"Финансовый результат:  {comment} {profit}")

if profit > 0:
    profitability = int(profit/expence)
    print(f"Рентабельность:  {profitability}")
    staff = int(input("Укажите число сотрудников: "))
    profit_staff = profit/staff
    print (f"Прибыль в расчёте на одного сотрудника:  {profit_staff}")