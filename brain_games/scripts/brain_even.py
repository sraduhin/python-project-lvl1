#!/usr/bin/env python3
import prompt
import random


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def is_Even(number):
    return True if number % 2 == 0 else False


def game():
    question = random.randint(0, 100)
    print('Question: ', question)
    answer = prompt.string('Your answer: ')
    return (question, answer)


def main():
    """Welcome to the Brain Games!
        May I have your name? Bill
        Hello, Bill!
        Answer "yes" if the number is even, otherwise answer "no".
        Question: 15
        Your answer: yes"""

    name = welcome_user()

    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        (question, answer) = game()
        correct_answer = 'yes' if is_Even(question) else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. \
Correct answer was \'{correct_answer}\'. \nLet\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
    return


if __name__ == '__main__':
    main()
