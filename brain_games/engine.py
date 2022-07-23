#!/usr/bin/env python3
import prompt


def engine(game_description, game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_description)
    for _ in range(3):
        question, correct_answer = game()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'. \nLet\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
    return


if __name__ == "__main__":
    engine('Always say "yes"', ('yes? ', 'yes'))