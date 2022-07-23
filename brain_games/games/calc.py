#!/usr/bin/env python3
import random
from brain_games.engine import engine


def get_correct_answer(value1, value2, operation):
    if operation == '+':
        return (value1 + value2)
    elif operation == '-':
        return (value1 - value2)
    elif operation == '*':
        return (value1 * value2)
    else:
        raise ValueError(f'operation {operation} is not supported')


description = 'What is the result of the expression?'


def game():
    random_value1 = random.randint(0, 50)
    random_value2 = random.randint(0, 10)
    random_operator = '+-*'[random.randint(0, 2)]
    question = f'{random_value1} {random_operator} {random_value2}'
    correct_answer = str(get_correct_answer(random_value1, random_value2,
                                            random_operator))
    return question, correct_answer


def main():
    engine(description, game)
    return
