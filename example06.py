a = int(input("Введите результаты пробежки первого дня в км "))
b = int(input("Введите общий желаемый результат в км "))

result_days = 1

while a < b:
        result_days += 1
        a += a * 0.10
else:
        print(f"Вы достигнете требуемых показателей на %.d день" % result_days)
