#!/usr/bin/env python3
import random
from brain_games.engine import engine


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = random.randint(0, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
