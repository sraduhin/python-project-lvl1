#!/usr/bin/env python3
import random
from brain_games.engine import engine


def get_correct_answer(value1, value2):
    if value2 == 0:
        return value1
    return get_correct_answer(value2, value1 % value2)


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    range = (0, 100)
    (start, end) = range
    random_value1 = random.randint(start, end)
    random_value2 = random.randint(start, end)
    question = f'{random_value1} {random_value2}'
    correct_answer = str(get_correct_answer(random_value1, random_value2))
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
