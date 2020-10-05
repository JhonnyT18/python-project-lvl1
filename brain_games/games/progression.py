# -*- coding: utf-8 -*-


from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_data_for_game():
    begin_of_progression = 1
    end_of_progression = 100
    step_of_progression = randint(1, 10)
    lenght_of_progression = 10
    progression = [i for i in range(begin_of_progression, end_of_progression, step_of_progression)][0:lenght_of_progression]  # noqa: E501
    index_deleted_number = randint(begin_of_progression, len(progression) - 1)  # noqa: E501
    correct_answer = progression[index_deleted_number]
    progression.pop(index_deleted_number)
    progression.insert(index_deleted_number, '..')
    question = ''
    for i in progression:
        question += str(i) + ' '
    return question, str(correct_answer)
