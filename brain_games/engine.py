#!/usr/bin/env python3
import prompt


def engine(game_description, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_description)
    ROUNDS_COUNT = 3
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'."
                  .format(answer, correct_answer))
            print('Let\'s try again, {}!'.format(name))
            return
    print(f'Congratulations, {name}!')
