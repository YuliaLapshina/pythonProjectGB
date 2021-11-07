#версия задания2 самостоятельно выполненная
time_sec = int(input("Время в секундах: "))
time_sec_correct = time_sec % 60
time_min = time_sec // 60
time_min_correct = time_min % 60
time_hour = time_min // 60
time_hour_correct = time_hour % 24
time_day = time_hour // 24

print(f"{time_day} дней {time_hour_correct:02}:{time_min_correct:02}:{time_sec_correct:02}")
