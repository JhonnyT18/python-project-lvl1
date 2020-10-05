# -*- coding: utf-8 -*-


from random import randint


GAME_DESCRIPTION = 'Answer "yes" if number even otherwise "no".'


def get_data_for_game():
    number = randint(0, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    question = str(number)
    return question, str(correct_answer)
