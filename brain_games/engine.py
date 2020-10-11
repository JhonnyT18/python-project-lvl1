# -*- coding: utf-8 -*-


import prompt


def play_game(game):
    print('Welcome to the Brain Games!')
    print(game.GAME_DESCRIPTION)
    print()
    name = prompt.string('May I have your name? ')
    print('Hello, {}!\n'.format(name))
    counter = 0
    quantity_of_rounds = 3
    while counter < quantity_of_rounds:
        question, correct_answer = game.get_data_for_game()
        print('Question: ' + question)
        answer_of_user = prompt.string('Your answer: ')
        if answer_of_user == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer_of_user, correct_answer))  # noqa: E501
            print("Let's try again, {}!".format(name))
            break
        counter += 1
    else:
        print("Congratulations, " + name + "!")
