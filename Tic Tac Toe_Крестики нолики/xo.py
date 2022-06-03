import os
from xointer import interface

def xoo():
    d = [0, 1, 2]
    a = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    os.system('clear')  
    error = ''
    xo = 1
    while xo != 10:
        if xo % 2 != 0:
            s = 'x'
        else:
            s = 'o'
        if a[0][0]==a[0][1]==a[0][2]!=' ' or a[1][0]==a[1][1]==a[1][2]!=' ' or a[2][0]==a[2][1]==a[2][2]!=' ' or a[0][0]==a[1][1]==a[2][2]!=' ' or a[2][0]==a[1][1]==a[0][2]!=' ' or a[0][0]==a[1][0]==a[2][0]!=' ' or a[0][1]==a[1][1]==a[2][1]!=' ' or a[0][2]==a[1][2]==a[2][2]!=' ':
            interface(a)
            print('Вы выиграли')
            xo = 10
        elif xo == 9:
            interface(a)
            print('Ничья! Победила дружба ')
            xo = 10
        else:
            interface(a)
            print(f'Ход {s}')
            print(error)
            stroka = input('Введите строку: ')
            stolb = input('Введите столбец: ')
            j = 0
            if stroka.isdigit() and stolb.isdigit():
                stolb = int(stolb)
                stroka = int(stroka)
                while j == 0:
                    if 3 > stolb >= 0 and 3 > stroka >= 0 and a[stroka][stolb] == ' ':
                        a[stroka][stolb] = s
                        os.system('clear')                
                        j =1
                        xo += 1
                        error = ''
                    else:
                        os.system('clear')
                        error = 'Поле занято, либо неправильные координаты'
                        j = 1
            else:
                os.system('clear')
                error = 'Введите именно числа'


xoo()