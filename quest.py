
x = input("Введите число: ")
flag = False

if x.isnumeric() and int(x) <= 9:                   # Фильтр вводимых данных
    print('NO')
else:
    flag = True
    xwork = int(x)
    x11 = int(len(x)*"1")

while flag == True:
    if (xwork-x11) > 0 and len(str(x11)) > 1:       # Проверка неотрицательного ответа и соответствия x11
        xwork = xwork - x11
    elif (xwork-x11) < 0:                           # Коррекция x11
        x11 = int(str(x11)[:-1])
    elif xwork == 0 or xwork % 11 == 0:             # Проверка возможности правильного ответа
        print('YES')
        break
    else:
        print('NO')                                 # Вывод отрицательного ответа

