import random

input('Введите имя: ')
select = input('Хотители поиграть?(да, нет): ')
i = 0
while i == 0:
    if select == 'да' or select == 'Да':
        num = random.randint(0, 10)
        print(num) #для проверки
        j = 0
        count = 0
        while j == 0:
            user_num = input('Введите число от 0-10: ')
            if user_num.isdigit():
                user_num = int(user_num)
                if num == user_num:
                    select = input(f'Вы угадали за {count+1} попыток \nХотители поиграть еще раз?: ')
                    j = 1
                elif num != user_num:
                    count += 1
            else:
                print('Вы ввели не цифру')
    elif select == 'нет' or select == 'Нет':
        print('Програма закрыта')
        i = 1
    else:
        print('Введите именно да или нет: ')
        select = input('Хотители поиграть?(да, нет): ')