import random
from confirm_input import confirm_input


class RollTheDice:

    def __init__(self):
        self.status = None
        self.num_sides = 6

    def _roll(self):
        self.status = random.randint(1, self.num_sides)
        print(f"The result of your roll is: {self.status}")

    def _get_user_input(self):
        user_input = input("Enter 'Roll' to roll the dice, 'Home' to return to"
                           " home screen, or 'Quit' to quit: ")
        return user_input.lower()

    def run(self):
        print("Hello! Welcome to the 'Roll the Dice' feature!")
        task = None
        while task != 'home' and task != 'quit':
            task = self._get_user_input()
            if task == 'roll':
                self._roll()
            elif task != 'home' and task != 'quit':
                print("Oops! Input not recognized. Please Try again.")
            else:
                task = confirm_input(task)

        return task
