# -*- coding: utf-8 -*-


import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    question, correct_answer = game.get_data_for_game()
    print(game.GAME_DESCRIPTION)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    print('Question: ' + question)
    answer_of_user = prompt.string('Your answer: ')
    counter = 1
    quantity_right_answers_to_get_congratulations = 3
    while answer_of_user == correct_answer and counter < quantity_right_answers_to_get_congratulations:  # noqa: E501
        print('Correct!')
        question, correct_answer = game.get_data_for_game()
        print('Question: ' + question)
        answer_of_user = prompt.string('Your answer: ')
        counter += 1
    if answer_of_user != correct_answer:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer_of_user, correct_answer))  # noqa: E501
        print("Let's try again, {}!".format(name))
    else:
        print("Correct!\nCongratulations, " + name + "!")
