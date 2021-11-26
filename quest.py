def x11(x):
    try:
        int(x)
    except ValueError:
        return 'This is string!'
    if not x.isnumeric() or int(x) <= 10:					# Фильтр вводимых данных
        return 'Invalid number or string'
    else:
        xwork = int(x)
        x11 = int(len(x)*"1")

    while True:
        if (xwork-x11) > 0 and len(str(x11)) > 1 and xwork % 11 != 0:		# Проверка неотрицательного ответа и соответствия x11
            xwork = xwork - x11
        elif (xwork-x11) < 0:                                               	# Коррекция x11
            x11 = int(str(x11)[:-1])
        elif xwork == 0 or xwork % 11 == 0 or (xwork-x11) == 0:             	# Проверка возможности правильного ответа
            return 'YES'
        else:
            return 'NO'

def test1m(x):                      						# Проверка чисел до 1000000
    answers = [0, 0, 0]
    print('Программа запущена...')
    for i in range(int(x)):
            if x11(i) == 'YES':
                answers[0] += 1
            elif x11(i) == 'NO':
                answers[1] += 1
            else:
                answers[2] +=1
    print('yes: ', answers[0])
    print('no: ', answers[1])
    print('worng: ', answers[2])
    return ''

#print('Введите конец диапазона тестирования (0-...): ',end='')
#print(test1m(input()))

print(x11(input()))
