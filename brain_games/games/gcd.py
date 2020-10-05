# -*- coding: utf-8 -*-


from random import randint


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_gcd(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    gcd = first_number + second_number
    return gcd


def get_data_for_game():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    question = '{} {}'.format(first_number, second_number)
    correct_answer = find_gcd(first_number, second_number)
    return question, str(correct_answer)
