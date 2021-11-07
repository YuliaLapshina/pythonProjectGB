a = float(input("Дистанция в первый день (км): "))
b = float(input("Целевая дистанция (км): "))
days = 1
while a < b:
    a = a + a*0.1
    days = days + 1

print(f"Потребуется еще {days} дней")
