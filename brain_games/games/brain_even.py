# -*- coding: utf-8 -*-


from random import randint


def brain_even():
    QUESTION_STRING = 'Answer "yes" if number even otherwise "no".\n'
    x = randint(0, 100)
    if x % 2 == 0:
        correct_answer = 'yes'
    elif x % 2 > 0:
        correct_answer = 'no'
    question = str(x)
    return QUESTION_STRING, question, correct_answer
