#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games.games import brain_calc
from brain_games.games import brain_even
from brain_games.games import brain_gcd
from brain_games.games import brain_prime
from brain_games.games import brain_progression
from brain_games import ask


def play_game(game):
    name, answers = game()
    counter = 1
    if answers[2] is False:
        print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
    while answers[2] is True and counter < 3:
        if game == brain_calc.brain_calc:
            answers = ask.ask_for_calc()
        elif game == brain_even.brain_even:
            answers = ask.ask_to_user()
        elif game == brain_gcd.brain_gcd:
            answers = ask.GCD()
        elif game == brain_prime.brain_prime:
            answers = ask.is_prime()
        elif game == brain_progression.brain_progression:
            answers = ask.progression()
        counter += 1
        if answers[2] is True and counter >= 3:
            print("Congretulations, " + name + "!")
        elif answers[2] is False:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.\nLet's try again, {}!".format(answers[1], answers[0], name))  # noqa: E501
