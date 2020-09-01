#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_prime():
    first_greet.greet_for_prime()
    name = cli.welcome_user()
    answers = ask.is_prime()
    return name, answers
