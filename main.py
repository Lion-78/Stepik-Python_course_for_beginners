# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# объявление функции


import random
global number_min, number_max


def is_valid(number_input):

    global number_min, number_max

    while True:
        if number_min <= number_input <= number_max:
            return True
        else:
            return False


def guess_number(num_min, num_max):

    num_gen = random.randint(num_min, num_max)
    play = True
    counter_attempts = 0
    while play:
        print('Введите число')
        num_input = int(input())
        counter_attempts += 1
        if is_valid(num_input):
            if num_input == num_gen:
                print('Вы угадали, поздравляем!')
                print('Количество попыток равно', counter_attempts)
                return
            elif num_input > num_gen:
                print('Слишком много, попробуйте еще раз')
            else:
                print('Слишком мало, попробуйте еще раз')
        else:
            print('А может все-таки введете целое число в диапазоне от', number_min, 'до', number_max)


def continue_game():
    print()
    print('Хотите сыграть ещё?')
    print(
        """Нажмите 'д' (да) или 'у' (yes), если хотите продолжить.
        Или 'н' (нет) или 'n' (no) , если хотите закончить""")
    while True:
        play_yet = input()
        if play_yet.lower() in ('y', 'д'):
            return True
        elif play_yet.lower() in ('n', 'н'):
            return False
        else:
            print("""Только 'д' (да) или 'у' (yes), если хотите продолжить., '\n', 
            Или 'н' (нет) или 'n' (no), если хотите закончить""")


# Функция основная игры
def game():

    global number_min, number_max

    print('Добро пожаловать в числовую угадайку!')
    print('Введите 2 числа, границы диапазона в котором будете угадывать числа')
    number_min, number_max = int(input()), int(input())
    while True:
        guess_number(number_min, number_max)
        if not continue_game():
            print('Конец игры')
            print('До скорой встречи!')
            break


# Вызов основной функции

game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
