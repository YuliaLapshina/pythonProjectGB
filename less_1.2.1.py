#версия задания2, разобранная на уроке

time_sec = int(input("Время в секундах: "))

if time_sec < 60:
    print(f"00:00:{time_sec:02}")
elif time_sec < 3600:
    print(f"00:{time_sec//60:02}:{time_sec % 60:02}")
else:
    print (f"{time_sec // 3600:02}:{time_sec % 3600// 60:02}:{time_sec % 60:02}")
