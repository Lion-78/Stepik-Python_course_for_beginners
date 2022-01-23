# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


def repeat_game():
    repeat = input('Есть ещё вопросы? Y/N (Д/Н):\n').upper()
    if repeat in ('Y', 'Д'):
        return True
    elif repeat in ('N', 'Н'):
        return False
    else:
        print('Не понял твой ответ. Правильный ответ Д (Y) или Н (N).')
        repeat_game()


# объявление функций
def game_magic_ball():
    answers = ('Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определенно да', 'Можешь быть уверен в этом',
               'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
               'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать',
               'Сконцентрируйся и спроси опять',
               'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие',
               'Весьма сомнительно')
    print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
    username = input('Введите свое имя, пожалуйста.\n')
    print('Привет,', username)
    play = True
    while play:
        print()
        question = input('Задайте свой вопрос.\n')
        while question == '':
            print()
            question = input('Задайте свой не пустой вопрос.\n')
        print(random.choice(answers))
        print()
        print('Хотите продолжить?')
        if repeat_game():
            continue
        else:
            print()
            print('Возвращайся если возникнут вопросы!')
            break


# вызываем функцию
game_magic_ball()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
