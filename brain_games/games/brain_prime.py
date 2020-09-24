# -*- coding: utf-8 -*-


from random import randint


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'  # noqa: E501


first_known_prime = 2


def make_answer_for_prime(number):
    if number == first_known_prime:
        correct_answer = 'yes'
    else:
        for i in range(first_known_prime, number):
            if number % i == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    return correct_answer


def get_data_for_game():
    number = randint(first_known_prime, 100)
    correct_answer = make_answer_for_prime(number)
    question = str(number)
    return question, correct_answer
