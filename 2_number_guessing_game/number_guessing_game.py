from random import randint

lower_num, higher_num = 1, 10
randon_numer: int = randint(lower_num, higher_num)
print(f'Guess the number in the range of {lower_num} and {higher_num}.')

while True:
    try:
        user_input: int = int(input('Enter your guess: '))
    except ValueError as e:
        print(f"Please enter a valid number. {e}")
        continue

    if user_input > randon_numer:
        print("the number is lower")
    elif user_input < randon_numer:
        print("the number is higher")
    else:
        print(f"You guessed the number {randon_numer} correctly!")
        break
