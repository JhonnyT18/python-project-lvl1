welcome = 'Welcome to the Brain Games!'


def greet():
    print(welcome)


def greet_for_even():
    print('{}\nAnswer "yes" if number even otherwise "no".'.format(welcome))


def greet_for_calc():
    print('{}\nWhat is the result of the expression?'.format(welcome))


def greet_for_gcd():
    print('{}\nFind the greatest common divisor of given numbers.'.format(welcome))  # noqa: E501


def greet_for_progression():
    print('{}\nWhat number is missing in the progression?'.format(welcome))


def greet_for_prime():
    print('{}\nAnswer "yes" if given number is prime. Otherwise answer "no".'.format(welcome))  # noqa: E501
