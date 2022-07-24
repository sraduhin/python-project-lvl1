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
    range_first_element_of_progression = (0, 100)
    range_ster_progression = (1, 9)
    range_length_progression = (6, 10)
    (start, end) = range_first_element_of_progression
    start_value = random.randint(start, end)
    (start, end) = range_ster_progression
    step_progression = random.randint(start, end)
    (start, end) = range_length_progression
    length_progression = random.randint(start, end)
    hidden_index = random.randint(0, length_progression - 1)
    progression = make_progression(start_value, step_progression,
                                   length_progression)
    correct_answer = str(start_value + step_progression * hidden_index)
    question = progression.replace(correct_answer, '..')
    return question, correct_answer


def main():
    engine(DESCRIPTION, generate_round)
