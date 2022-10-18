from flip_a_coin import FlipACoin
from roll_the_dice import RollTheDice
from choose_a_card import ChooseACard
from confirm_input import confirm_input


class RandomApp:

    def __init__(self):
        self.features = [
            ('Flip a Coin', FlipACoin),
            ('Roll the Dice', RollTheDice),
            ('Choose a Card', ChooseACard)
        ]

    def _choose_feature(self):
        print("Here is a list of options to choose from:")
        print("0 - Quit")
        for i, feature in enumerate(self.features):
            print(f"{i+1} - {feature[0]}")
        choice = -1
        while not 0 <= choice <= len(self.features):
            try:
                choice = int(input("Please enter the number of a feature above"
                                   " to select a feature: "))
                if not 0 <= choice <= len(self.features):
                    print("Oops! The number you entered is not within the"
                          " available range.")
            except ValueError:
                print("Oops! You did not enter an integer.")

        if choice == 0:
            return

        return self.features[choice - 1][1]

    def run(self):
        print("Welcome to my randomizer app!")
        while True:
            go_next = 'quit'
            feature_class = self._choose_feature()
            if feature_class is not None:
                feature_instance = feature_class()
                go_next = feature_instance.run()
                if go_next == 'quit':
                    break
            if go_next == 'quit':
                go_next = confirm_input(go_next)
            if go_next == 'quit':
                break
        print("Thank you for using my randomizer app!")


if __name__ == '__main__':
    app = RandomApp()
    app.run()
