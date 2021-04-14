import random as rdm


def guess(x):
    rdm_number = rdm.randint(1, x)
    guess = 0
    while guess != rdm_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < rdm_number:
            print('Guess again. Your guess number was too low!')
        elif guess > rdm_number:
            print('Guess again. Your guess number was too high!')


    print(f"You've guessed right!!! The random number is {rdm_number}")

#guess(100)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        guess = rdm.randint(low, high)
        feedback = input(f'Is {guess} too high (H), too low (L), or correct(C)?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print(f'The computer has guessed your number {guess} correctly')

computer_guess(1000)