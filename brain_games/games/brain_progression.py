# -*- coding: utf-8 -*-


from random import randint


def brain_progression():
    QUESTION_STRING = 'What number is missing in the progression?\n'
    result = [i for i in range(1, 100, randint(1, 10))]
    progression = [result[i] for i in range(10)]
    deleted_charecter = randint(0, 9)
    correct_answer = progression[deleted_charecter]
    progression.pop(deleted_charecter)
    progression.insert(deleted_charecter, '..')
    final_progression = ''
    for i in progression:
        final_progression += str(i) + ' '
    question = final_progression
    return QUESTION_STRING, question, correct_answer
