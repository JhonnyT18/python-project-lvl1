# -*- coding: utf-8 -*-


from random import randint


def brain_prime():
    QUESTION_STRING = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'  # noqa: E501
    x = randint(2, 100)
    question = str(x)
    if x == 2:
        correct_answer = 'yes'
    else:
        for i in range(2, x):
            if x % i == 0:
                correct_answer = 'no'
                break
            else:
                correct_answer = 'yes'
    return QUESTION_STRING, question, correct_answer
