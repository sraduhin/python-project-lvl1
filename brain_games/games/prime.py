#!/usr/bin/env python3
import random
from brain_games.engine import engine


RANDOM_VALUE_LIMITS = (0, 100)
DESCRIPTION = 'Answer "yes" if the number is prime, otherwise answer "no".'


def is_prime(value):
    if value < 2:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


def generate_round():
    (start, end) = RANDOM_VALUE_LIMITS
    question = random.randint(start, end)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
