# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
global symbols_list


def generate_symbols_list(include_num, include_lo_letters, include_up_letters, include_spec, not_include_ambig_chars):
    global symbols_list
    numbers = list(range(10)) * 3
    letters_lower = [chr(i) for i in range(97,123)]
    letters_upper = [chr(i) for i in range(65,91)]
    specials = list('!#$%&*+-=?@^_' * 3)
    ambiguos = list('il1Lo0O')

    symbols_list = []
    if include_num:
        symbols_list.append(numbers)
    if include_lo_letters:
        symbols_list.append(letters_lower)
    if include_up_letters:
        symbols_list.append(letters_upper)
    if include_spec:
        symbols_list.append(specials)
    if not_include_ambig_chars:
        for i in range(len(symbols_list)):
            for x in ambiguos:
               symbols_list[i].remove(x)
        # временно для проверки правильности составления списка списков допустимых символов
    print(symbols_list)
    return symbols_list

def generate_password(length_, count_):
    global symbols_list
    generate_symbols_list(include_num, include_lo_letters, include_up_letters, include_spec, not_include_ambig_chars)
    exit_ = [] # Список паролей
    for _ in range(count_):
        result = []
        for kit in symbols_list:
            result += random.sample(kit, length_)
            while len(result) - length_ > 0:
                del result[random.randint(1, len(result)-1)]
            exit_.append(result)
#        for i in range(len(exit_)):
#            random.shuffle(exit_[i])
        exit_ = [''.join(str(x) for x in i) for i in exit_]
    return exit_

def enter_numbers():
    print('Введите длину одного пароля:(минимум 6, максимум 20)')
    while True:
        length = input()
        if length.isdigit():
            length = int(length)
            if 6 <= int(length) <= 20:
                break
            else:
                print('Вы должны ввести число (минимум 6, максимум 20)!')
        else:
            print('Вы должны ввести число (минимум 6, максимум 20)!')
    print('Введите количество паролей, которые вы хотите сгенерировать')
    while True:
        count = input()
        if count.isdigit():
            count = int(count)
            if 0 < int(count) <= 20:
                break
            else:
                print('Вы должны ввести число (максимум 20)!')
        else:
            print('Вы должны ввести число (максимум 20)!')
    return length, count


print('Добро пожаловать в генератор паролей!\n')
length, count = enter_numbers()
include_num = input('Пароль должен включать цифры? [да/нет]').lower() == 'да'
include_up_letters = input('Пароль должен включать заглавные буквы?[да/нет]').lower() == 'да'
include_lo_letters = input('Пароль должен включать прописные буквы?[да/нет]').lower() == 'да'
include_spec = input('Пароль должен включать специальные символы !#$%&*+-=?@^_? [да/нет]').lower == 'да'
not_include_ambig_chars = input('Исключать неоднозначные символы il1Lo0O ?[да/нет]').lower == 'да'
symbols_list = generate_symbols_list(include_num, include_lo_letters, include_up_letters, include_spec, not_include_ambig_chars)
#print(symbols_list)
print('Ваши пароли: ', *generate_password(length, count), sep='\n')
