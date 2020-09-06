# -*- coding: utf-8 -*-


import prompt
from brain_games import cli


def play_game(game):
    print('Welcome to the Brain Games!')
    QUESTION_STRING, question, correct_answer = game()
    print(QUESTION_STRING)
    name = cli.welcome_user()
    print('Question: ' + question)
    answer_of_user = prompt.string('You answer: ')
    answers = [str(correct_answer), str(answer_of_user)]
    if answers[1] == answers[0]:
        answers.append(True)
    else:
        answers.append(False)
    counter = 1
    if answers[2] is False:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
    while answers[2] is True and counter < 3:
        print('Correct!')
        QUESTION_STRING, question, correct_answer = game()
        print('Question: ' + question)
        answer_of_user = prompt.string('You answer: ')
        answers = [str(correct_answer), str(answer_of_user)]
        if answers[1] == answers[0]:
            answers.append(True)
        else:
            answers.append(False)
        counter += 1
        if answers[2] is True and counter >= 3:
            print("Correct!\nCongretulations, " + name + "!")
        elif answers[2] is False:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
