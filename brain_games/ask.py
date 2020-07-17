import prompt
from random import choice
from random import randint


def ask_to_user():
    x = randint(0, 100)
    if x % 2 == 0:
        correct_answer = 'yes'
    elif x % 2 > 0:
        correct_answer = 'no'
    print('Question: ' + str(x))
    answer = prompt.string('Your answer: ')
    answers = [correct_answer, answer]
    if answers[1] == answers[0]:
        print('Correct!')
        answers.append(True)
    else:
        answers.append(False)
    return answers


def ask_for_calc():
    a = randint(0, 100)
    b = randint(0, 100)
    operator = [' + ', ' - ', ' * ']
    our_operator = choice(operator)
    print('Question: ' + str(a) + our_operator + str(b))
    if our_operator == ' + ':
        result = a + b
    elif our_operator == ' - ':
        result = a - b
    elif our_operator == ' * ':
        result = a * b
    answer = prompt.string('Your answer: ')
    answers = [str(result), answer]
    if answers[0] == answers[1]:
        print('Correct!')
        answers.append(True)
    else:
        answers.append(False)
    return answers


def GCD():
    a = randint(0, 100)
    b = randint(0, 100)
    print('Question: {} {}'.format(a, b))
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    result = a + b
    answer = prompt.string('Your answer: ')
    answers = [str(result), answer]
    if answers[1] == answers[0]:
        print('Correct!')
        answers.append(True)
    else:
        answers.append(False)
    return answers
