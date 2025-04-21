import random

from typing import List


def roll_dice(amount: int = 2) -> List[int]:
    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    rolls: List[int] = []
    for i in range(amount):
        random_rol: int = random.randint(1, 6)
        rolls.append(random_rol)

    return rolls


def main():
    while True:
        try:
            user_input: str = (input("How many dice do you want to roll? "))

            if user_input.lower() == 'exit':
                print('thanks for playing')
                break

            print(roll_dice(int(user_input)))
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

