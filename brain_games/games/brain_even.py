#!/usr/bin/env python3


# -*- coding: utf-8 -*-


from brain_games import first_greet
from brain_games import cli
from brain_games import ask


def brain_even():
    first_greet.greet_for_even()
    name = cli.welcome_user()
    answers = ask.ask_to_user()
    return name, answers
