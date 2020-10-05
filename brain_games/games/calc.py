# -*- coding: utf-8 -*-


from random import choice
from random import randint


GAME_DESCRIPTION = 'What is the result of the expression?'


def get_data_for_game():
    first_number = randint(0, 100)
    second_number = randint(0, 100)
    operators = ['+', '-', '*']
    current_operator = choice(operators)
    question = "{} {} {}".format(str(first_number), current_operator, str(second_number))  # noqa: E501
    if current_operator == operators[0]:
        correct_answer = first_number + second_number
    elif current_operator == operators[1]:
        correct_answer = first_number - second_number
    elif current_operator == operators[2]:
        correct_answer = first_number * second_number
    return question, str(correct_answer)
