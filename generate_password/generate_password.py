# -*- coding: utf-8 -*-
import random
lowle = [chr(i) for i in range(97, 123)]
uple = [chr(i) for i in range(65, 91)]
digits = list(range(10))*3
other = list('!#$%&*+-=?@^_'*3)
gen = []

def password_gen(length_: int, count_: int):
    exit_ = []
    for i in range(count_):
        result = []
        for kit in gen:
            result += random.sample(kit, length_)
        while (len(result) - length_) > 0:
            del result[random.randint(1, len(result)-1)]
        exit_.append(result)
    for i in range(len(exit_)):
        random.shuffle(exit_[i])
    exit_ = [''.join(str(x) for x in i) for i in exit_]
    return exit_


count = int(input('Сколько паролей вы хотите сгенерировать? '))
length = int(input('Введите длину одного пароля, до 20 символов: '))
print('На следующие вопросы отвечайте "да" или "нет"')
if input('Пароль должен включать цифры? ').lower() == 'да':
    gen.append(digits)
if input('Пароль должен включать строчные буквы? ').lower() == 'да':
    gen.append(lowle)
if input('Пароль должен включать прописные буквы? ').lower() == 'да':
    gen.append(uple)
if input('Пароль должен включать другие символы? ').lower() == 'да':
    gen.append(other)

print(*password_gen(length, count), sep='\n')
