num = int(input("Введите целое положительное число: "))
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
        print(max_num)
        if max_num == 9:
            break

    num //= 10

print(f"Наибольшая цифра числа: {max_num}")
