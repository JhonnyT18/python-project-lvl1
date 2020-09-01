#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_progression():
    first_greet.greet_for_progression()
    name = cli.welcome_user()
    answers = ask.progression()
    return name, answers
