# IntInputOnly() возвращает число или False, если введена строка или неправильная дробь
# x11() основной рабочий цикл. Принимает количество итераций и тестируемые числа

def IntInputOnly(data):
    if data == '':
        print('Пустой ввод.')
        return False
    try:
        data = float(data)
    except ValueError:
        print('Это строка!')
        return False
    if (data % 1) != 0:
        print('Неправильная дробь!')
        return False
    elif data < 0:
        print('Меньше нуля!')
        return False
    else:
        return int(data)


def x11(t):
    for i in range(IntInputOnly(t)):
        x = IntInputOnly(input('Введите число #' + str(i + 1) + ': '))
        # Фильтр вводимых данных
        if int(x) > 11:
            xwork = int(x)
            x11 = int(len(str(x)) * "1")
        elif not x:
            continue
        else:
            print('Слишком маленькое число (< 11)')
            continue
        while True:
            # Проверка неотрицательного ответа и соответствия x11
            if (xwork - x11) >= 0 and x11 >= 11 and xwork % 11 != 0:
                # print('Вычитание ', xwork, '-', x11)
                xwork = xwork - x11
            # Коррекция x11
            elif (xwork - x11) < 0 and not x11 < 11:
                # print('Коррекция')
                x11 = int(str(x11)[:-1])
            # Проверка возможности правильного ответа
            elif xwork == 0 or xwork % 11 == 0:
                # print('Подтверждение')
                print('YES')
                break
            else:
                # print('Отрицание')
                print('NO')
                break
    return ''


print(x11(input('Введите количество параметров: ')))
