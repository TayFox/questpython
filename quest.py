def x11(x):
    if x.isnumeric() and int(x) <= 9:                   # Фильтр вводимых данных
        return 'NO'
        flag = False
    else:
        flag = True
        xwork = int(x)
        x11 = int(len(x)*"1")

    while flag:
        if (xwork-x11) > 0 and len(str(x11)) > 1:       # Проверка неотрицательного ответа и соответствия x11
            xwork = xwork - x11
        elif (xwork-x11) < 0:                           # Коррекция x11
            x11 = int(str(x11)[:-1])
        else:
            return 'NO'
        if xwork == 0 or xwork % 11 == 0:  # Проверка возможности правильного ответа
            return 'YES'
print(x11(input('Введите число: ')))
