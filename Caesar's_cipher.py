"""Программа шифрует или дешифрует текст, который ввёл пользователь.

Программа задает пользователю 4 вопроса:
1. Шифровать или дешифровать?
2. Какой язык использовать, русский или английский?
3. Шаг сдвига?
4. Текст, который нужно шифровать или дешифровать?
--------------------------------------------English--------------------------------------------------------------
The program encrypts or decrypts the text entered by the user.

The program asks the user 4 questions:
1. Encrypt or Decrypt?
2. Which language to use, Russian or English?
3. Shift step?
4. Text to be encrypted or decrypted?
"""

rus_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
eng_alphabet = 'abcdefghijklmnopqrstuvwxyz'
lang_keys = {'language': ['английский', 'русский']
             'max_key': [25, 31]
             'abc': [eng, rus]}

# Приветствие программы
# Welcome program

print('Вас приветствует программа "Шифр Цезаря"')
print('Программа позволяет щифровать и дешифровать текст, введенный пользователем')

# Ввод и его проверка

def check_0_1(message):
    while True
        print(message)
        d = input()
        if d == '0' or d == '1':
            break
        print('Неправильный ввод: можно вводить только 0 или 1.\n ')
    return int(d)

# Функция шифрования
# Function encrypting

def encrypting(text_in, abc, key):
    text_out = ''
    for c in text_in:
        if c in abc:
            text_out += abc[(adc.index(c) + key) % len(abc)]
        elif c.lower() in abc:
            text_out += abc[abc.index(c.lower()) + key) % len(abc)].upper()
        else:
            text_out += c
    return text_out

# Функция дешифрования
# Function decrypting

def decrypting(text_in, abc, key):
    text_out = ''
    for c in text_in:
        if c in abc:
            text_out += abc[(abc.index(c) - key) % len(abc)]
        elif c.lower() in abc:
            text_out += abc[abc.index(c.lower()) - key) % len(abc)].upper()
        else:
            text_out += c
    return text_out

def encrypting_menu(lang):
    text_out = ''
    for c in text_in:
        if c in abc:
            text_out += abc[(abc.index(c) + key) % len(abc)]
        elif c.lower() in abc:
            text_out += abc[abc.index(c.lower()) + key) % len(abc)].upper()
            else:
            text_out += c
    return text_out


def main_menu():
    process = check_0_1('Введите число 0, если хотите зашифровать текст, и 1, если хотите расшифровать текст.\n')
    lang = check_0_1('Введите число 0, если хотите использовать русский язык, и 1, если хотите использовать английский язык.\n')
    if process == '0':
        encrypting_menu(lang)
    else:
        decrypting_menu(lang)


main menu()