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


DESCRIPTION = 'What is the result of the expression?'


def generate_round():
    range = (0, 100)
    (start, end) = range
    random_value1 = random.randint(start, end)
    random_value2 = random.randint(start, end)
    random_operator = random.choice(['+', '-', '*'])
    question = f'{random_value1} {random_operator} {random_value2}'
    correct_answer = str(get_correct_answer(random_value1, random_value2,
                                            random_operator))
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
