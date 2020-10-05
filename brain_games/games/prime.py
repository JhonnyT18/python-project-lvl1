# -*- coding: utf-8 -*-


from random import randint
from math import sqrt


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


def is_prime(number):
    first_of_known_prime = 2
    if number < first_of_known_prime:
        return False
    for i in range(first_of_known_prime, int(sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def get_data_for_game():
    number = randint(-100, 100)
    question = str(number)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return question, correct_answer
