# -*- coding: utf-8 -*-


from random import randint


def brain_gcd():
    QUESTION_STRING = 'Find the greatest common divisor of given numbers.\n'
    a = randint(0, 100)
    b = randint(0, 100)
    question = '{} {}'.format(a, b)
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    correct_answer = a + b
    return QUESTION_STRING, question, correct_answer
