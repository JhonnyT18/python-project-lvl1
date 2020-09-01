#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_gcd():
    first_greet.greet_for_gcd()
    name = cli.welcome_user()
    answers = ask.GCD()
    return name, answers
