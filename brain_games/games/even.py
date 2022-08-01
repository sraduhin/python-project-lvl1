#!/usr/bin/env python3
import random
from brain_games.engine import engine


RANDOM_VALUE_LIMITS = (0, 100)
DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    (start, end) = RANDOM_VALUE_LIMITS
    question = random.randint(start, end)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
