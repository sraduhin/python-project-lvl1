#!/usr/bin/env python3
import random
from brain_games.engine import engine


def is_prime(value):
    if value < 2:
        return False
    for i in range(2, value):
        if value % i == 0:
            return False
    return True


description = 'Answer "yes" if the number is prime, otherwise answer "no".'


def game():
    question = random.randint(0, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer


def main():
    engine(description, game)
    return
