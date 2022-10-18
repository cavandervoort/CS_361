import random
from confirm_input import confirm_input


class FlipACoin:

    def __init__(self):
        self.status = None

    def _flip(self):
        if random.randint(0, 1) == 0:
            self.status = 'Tails'
        else:
            self.status = 'Heads'
        print(f"The result of your flip is: {self.status}")

    def _get_user_input(self):
        user_input = input("Enter 'Flip' to flip a coin, 'Home' to return to"
                           " home screen, or 'Quit' to quit: ")
        return user_input.lower()

    def run(self):
        print("Hello! Welcome to the 'Flip a Coin' feature!")
        task = None
        while task != 'home' and task != 'quit':
            task = self._get_user_input()
            if task == 'flip':
                self._flip()
            elif task != 'home' and task != 'quit':
                print("Oops! Input not recognized. Please Try again.")
            else:
                task = confirm_input(task)

        return task
