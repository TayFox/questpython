x = input("Введите число: ")
flag = False

if x.isnumeric() == False:		# Защита от дроби
    print('NO')
elif int(x) == 0:		 	# Защита от 0
    print('NO')
elif int(x) < 0:			# Защита от отрицательных чисел
    print('NO')
else:
    flag = True				# Присвоение значений
    xwork = int(x)
    x11 = int(len(x)*"1")
#    print('Полученное число: ',xwork)
#    print('Первый x11: ', x11)

while flag == True:
    if xwork > 0:
#        print('Новый цикл')
#        print(xwork,"-",x11)
        xwork = xwork - x11
#        print(xwork)
        if xwork < 0:			# Коррекция
#            print('Коррекция')
            xwork = xwork + x11
            x11 = str(x11)
            x11 = x11[:-1]
            if len(x11) <= 1:
#                print("x11 < 1 !!!")
#                print('NO')
                break
            x11 = int(x11)
#            print(x11)
        if xwork % 11 == 0:		# Проверка деления на 11
            print('YES')
            break
        else:
            continue
    elif xwork == 0:
        print('YES')
        break
    else:
        print('NO')
        break
