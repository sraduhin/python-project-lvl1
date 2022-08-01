import prompt


ROUNDS_COUNT = 3


def engine(game_description, generate_round):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print(game_description)
    for _ in range(ROUNDS_COUNT):
        question, correct_answer = generate_round()
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
