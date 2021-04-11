import random

from projects.higher_lower.arts import logo, vs
from projects.higher_lower.games_data import data


class HigherLower:
    @staticmethod
    def select_item():
        return random.choice(data)

    @staticmethod
    def print_card(card, label):
        print(
            f"Compare {label.upper()}: {card['name']}, a {card['description']}, from {card['country']}"
        )

    @staticmethod
    def who_has_more_followers(card_a, card_b):
        if card_a["follower_count"] > card_b["follower_count"]:
            answer = "A"
        elif card_a["follower_count"] > card_b["follower_count"]:
            answer = "B"
        else:
            answer = "Draw"
        return answer.upper()

    def display_vs_card(self, card_a, card_b):
        self.print_card(card_a, "a")
        print(vs)
        self.print_card(card_b, "b")

    def select_cards(self, card_a):
        while True:
            card_b = self.select_item()
            if card_a != card_b:
                break
        return card_a, card_b

    def start(self):
        print(logo)
        current_score = 0
        card_b = self.select_item()
        while True:
            card_a, card_b = self.select_cards(card_b)
            self.display_vs_card(card_a, card_b)
            guess = input("Who has more followers? Type 'A' or 'B': ").upper()
            answer = self.who_has_more_followers(card_a, card_b)
            if guess == answer:
                current_score += 1
                print(f"You're right! current score: {current_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {current_score}")
                break


if __name__ == "__main__":
    HigherLower().start()
