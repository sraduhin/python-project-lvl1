#!/usr/bin/env python3
import random
from brain_games.engine import engine


def get_correct_answer(value1, value2):
    if value2 == 0:
        return value1
    return get_correct_answer(value2, value1 % value2)


description = 'Find the greatest common divisor of given numbers.'


def game():
    random_value1 = random.randint(0, 100)
    random_value2 = random.randint(0, 100)
    question = f'{random_value1} {random_value2}'
    correct_answer = str(get_correct_answer(random_value1, random_value2))
    return question, correct_answer


def main():
    engine(description, game)
    return
