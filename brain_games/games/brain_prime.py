#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_prime():
    first_greet.greet_for_prime()
    name = cli.welcome_user()
    answers = ask.is_prime()
    counter = 1
    if answers[2] is False:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
    while answers[2] is True and counter < 3:
        answers = ask.is_prime()
        counter += 1
        if answers[2] is True and counter >= 3:
            print("Congretulations, " + name + "!")
        elif answers[2] is False:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
