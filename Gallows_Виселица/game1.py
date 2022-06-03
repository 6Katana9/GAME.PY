import getpass
import os
start = """
_____
▍   ◯ 
▍   
▍  
▍________
"""
a1 = r"""
_____
▍   ◯ 
▍   |
▍  
▍________
"""
a2 = r"""
_____
▍   ◯ 
▍  /|
▍  
▍________
"""
a3 = r"""
_____
▍   ◯ 
▍  /|\
▍  
▍________
"""
a4 = r"""
_____
▍   ◯ 
▍  /|\
▍  / 
▍________
"""
a5 = r"""
_________
▍        ▍
▍  game  ▍
▍  over  ▍
▍________▍
"""
os.system('clear')
list_hu = [start, a1,a2,a3,a4,a5]
i = 0
while i < 1:
    try:
        in_ = 0
        words = getpass.getpass(prompt='Загадайте слово: ')
        count = 5
        if words.isalpha()==False:
            raise Exception('Введите слово из букв')

    except Exception as e:
        print(e)
    
    else:
        os.system('clear')
        word = '*' * len(words)
        list_ = list(word)
        j = 0
        words = words.lower()
        while j < 1:
            if words == word:
                os.system('clear')
                print(f'Поздравляю, вы выиграли!!!\nЭто слово - {words}')
                j = 1
                i = 1
                print(list_hu[in_])
            elif count == 0:
                os.system('clear')
                print('К сожалению, вы проиграли!!!')
                i = 1
                j = 1
                print(list_hu[in_])
            else:
                print(word)
                letter = input('Введите букву: ')
                if letter.isalpha() and len(letter) == 1:
                    if letter in words:
                        os.system('clear')
                        word = ''
                        for l, v in enumerate(words):
                            if v == letter:
                                list_[l] = v
                        for i in list_:
                            word+=i
                        print(f'Такая буква есть!')
                        print(list_hu[in_])
                        
                    else:
                        os.system('clear')
                        count -= 1
                        in_ += 1
                        
                        print(f'Буквы {letter}, нету. У вас осталось {count} попыток')
                        print(list_hu[in_])
