# -*- coding: utf-8 -*-


from random import choice
from random import randint


def brain_calc():
    QUESTION_STRING = 'What is the result of the expression?\n'
    a = randint(0, 100)
    b = randint(0, 100)
    operator = [' + ', ' - ', ' * ']
    our_operator = choice(operator)
    question = str(a) + our_operator + str(b)
    if our_operator == ' + ':
        correct_answer = a + b
    elif our_operator == ' - ':
        correct_answer = a - b
    elif our_operator == ' * ':
        correct_answer = a * b
    return QUESTION_STRING, question, correct_answer
