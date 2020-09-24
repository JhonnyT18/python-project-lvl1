# -*- coding: utf-8 -*-


from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'


def get_data_for_game():
    begin_of_progression = 1
    end_of_progression = 100
    step_of_progression = randint(1, 10)
    progression = [i for i in range(begin_of_progression, end_of_progression, step_of_progression)]  # noqa: E501
    progression_length = 10
    ten_numbers_of_progression = [progression[i] for i in range(progression_length)]  # noqa: E501
    progression_first_index = 0
    progression_last_index = 9
    index_deleted_number = randint(progression_first_index, progression_last_index)  # noqa: E501
    correct_answer = progression[index_deleted_number]
    ten_numbers_of_progression.pop(index_deleted_number)
    ten_numbers_of_progression.insert(index_deleted_number, '..')
    final_progression = ''
    for i in ten_numbers_of_progression:
        final_progression += str(i) + ' '
    question = final_progression
    return question, str(correct_answer)
