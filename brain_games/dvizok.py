# -*- coding: utf-8 -*-


import prompt
from brain_games import cli


def play_game(game):
    print('Welcome to the Brain Games!')
    question, correct_answer = game.get_data_for_game()
    print(game.GAME_DESCRIPTION)
    print()
    name = cli.welcome_user()
    print('Question: ' + question)
    answer_of_user = prompt.string('You answer: ')
    if answer_of_user == correct_answer:
        answer_is_right = True
    else:
        answer_is_right = False
    counter = 1
    if answer_is_right is False:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer_of_user, correct_answer))  # noqa: E501
        print("Let's try again, {}!".format(name))
    while answer_is_right is True and counter < 3:
        print('Correct!')
        question, correct_answer = game.get_data_for_game()
        print('Question: ' + question)
        answer_of_user = prompt.string('You answer: ')
        if answer_of_user == correct_answer:
            answer_is_right = True
        else:
            answer_is_right = False
        counter += 1
        if answer_is_right is True and counter >= 3:
            print("Correct!\nCongretulations, " + name + "!")
        elif answer_is_right is False:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer_of_user, correct_answer))  # noqa: E501
            print("Let's try again, {}!".format(name))
