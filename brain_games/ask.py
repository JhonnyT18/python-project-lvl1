import prompt
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
