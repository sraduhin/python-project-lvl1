#!/usr/bin/env python3
import random
from brain_games.engine import engine


def make_progression(first_element, step, length):
    progression = []
    for i in range(length):
        current = first_element + step * i
        progression.append(str(current))
    return ' '.join(progression)


def get_correct_answer(value1, value2):
    if value2 == 0:
        return value1
    return get_correct_answer(value2, value1 % value2)


DESCRIPTION = 'What number is missing in the progression?'


def generate_round():

    RANGE_FIRST_ELEMENT_OF_PROGRESSION = (0, 100)
    RANGE_STEP_PROGRESSION = (1, 9)
    RANGE_LENGTH_PROGRESSION = (6, 10)

    (start, end) = RANGE_FIRST_ELEMENT_OF_PROGRESSION
    start_value = random.randint(start, end)
    (start, end) = RANGE_STEP_PROGRESSION
    step_progression = random.randint(start, end)
    (start, end) = RANGE_LENGTH_PROGRESSION
    length_progression = random.randint(start, end)
    hidden_index = random.randint(0, length_progression - 1)
    progression = make_progression(start_value, step_progression,
                                   length_progression)
    correct_answer = str(start_value + step_progression * hidden_index)
    question = progression.replace(correct_answer, '..')
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
