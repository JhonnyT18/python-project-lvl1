# -*- coding: utf-8 -*-


from random import choice
from random import randint


GAME_DESCRIPTION = 'What is the result of the expression?'


def get_data_for_game():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operators = [' + ', ' - ', ' * ']
    current_operator = choice(operators)
    question = str(first_number) + current_operator + str(second_number)
    if current_operator == ' + ':
        correct_answer = first_number + second_number
    elif current_operator == ' - ':
        correct_answer = first_number - second_number
    elif current_operator == ' * ':
        correct_answer = first_number * second_number
    return question, str(correct_answer)
