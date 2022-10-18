import random
from confirm_input import confirm_input


class ChooseACard:

    def __init__(self):
        self.status = None

        self._cards = []
        for number in ['Ace', '2', '3', '4', '5', '6',
                       '7', '8', '9', '10', 'Jack', 'Queen', 'King']:
            for suit in ['Spades', 'Hearts', 'Diamonds', 'Clubs']:
                self._cards.append(number + ' of ' + suit)

    def _choose(self):
        self.status = self._cards[random.randint(0, len(self._cards))]
        print(f"Your card is: {self.status}")

    def _get_user_input(self):
        user_input = input("Enter 'Choose' to choose a card, 'Home' to return"
                           " to home screen, or 'Quit' to quit: ")
        return user_input.lower()

    def run(self):
        print("Hello! Welcome to the 'Choose a Card' feature!")
        task = None
        while task != 'home' and task != 'quit':
            task = self._get_user_input()
            if task == 'choose':
                self._choose()
            elif task != 'home' and task != 'quit':
                print("Oops! Input not recognized. Please Try again.")
            else:
                task = confirm_input(task)

        return task
