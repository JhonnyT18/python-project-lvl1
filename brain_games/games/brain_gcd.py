#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_gcd():
    first_greet.greet_for_gcd()
    name = cli.welcome_user()
    answers = ask.GCD()
    counter = 1
    if answers[2] is False:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
    while answers[2] is True and counter < 3:
        answers = ask.GCD()
        counter += 1
        if answers[2] is True and counter >= 3:
            print("Congretulations, " + name + "!")
        elif answers[2] is False:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
