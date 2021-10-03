# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from random import randint

def play_again(answer):
    if answer.lower() in ('д', 'y'):
        return play_game(), True
    else:
        return False


def is_digit(num):
    if num.isdigit():
        return int(num)
    else:
        print('Введите число')
        return is_digit(input())


def play_game():
    guess_counter = 7
    n = randint(1, 100)
    print('''Попробуйте угадать число от 1 до 100. У Вас есть 7 попыток.\n'''
          '''Введите число:''')
    while True:
        player_guess = is_digit(str(input()))
        if guess_counter == 1:
            print(f'Попытки закончились, было загадано число {n}')
            break
        if 1 > player_guess > 100:
            print(f'Введенное число вне диапазона 1-100')
        elif player_guess > n:
            guess_counter -= 1
            print(f'Загаданное число меньше {player_guess}, осталось {guess_counter} попыток')
        elif player_guess < n:
            guess_counter -= 1
            print(f'Загаданное число больше {player_guess}, осталось {guess_counter} попыток')
        elif player_guess == n:
            print(f'Поздравляю! Вы угадали число {n}! c {8 - guess_counter}-й попытки')
            break


n = True
play_game()
while n:
    print('Хотите сыграть ещё раз? (д/н)')
    n = play_again(input())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
