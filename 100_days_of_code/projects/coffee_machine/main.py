import sys


class CoffeeMachine:
    earnings = 0
    MENU = {
        "espresso": {
            "ingredients": {
                "water": 50,
                "coffee": 18,
            },
            "cost": 1.5,
        },
        "latte": {
            "ingredients": {
                "water": 200,
                "milk": 150,
                "coffee": 24,
            },
            "cost": 2.5,
        },
        "cappuccino": {
            "ingredients": {
                "water": 250,
                "milk": 100,
                "coffee": 24,
            },
            "cost": 3.0,
        },
    }

    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    coins_operated = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    stored_coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}

    def make_front_panel_choice(self):
        drinks = "/".join(k for k in self.MENU)
        while True:
            choice = input(f"What would you like? ({drinks}): ").lower()
            if choice in self.MENU:
                break
            elif choice == "off":
                self.turn_off()
            elif choice == "report":
                self.print_report()
        return choice

    @staticmethod
    def turn_off():
        sys.exit()

    def print_report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")
        print(f"Money: ${self.earnings}")

    def check_resources_for_drink(self, drink):
        success = True
        for ingredient, required in drink["ingredients"].items():
            if self.resources[ingredient] < required:
                success = False
                print(f"Sorry, there is not enough {ingredient}")
                break
        return success

    def process_coins(self):
        coins = "/".join(k for k in self.coins_operated)
        inserted_coins = {}
        print("Please insert coins.")
        while True:
            # type_of_coin = ''
            while True:
                type_of_coin = input(f"Please select coin type to insert: ({coins}): ")
                if type_of_coin in self.coins_operated:
                    break
            number_of_coins = int(input(f"Number of {type_of_coin} inserted: "))
            inserted_coins[type_of_coin] = number_of_coins
            choose = input("Do you want to insert more coins? Type 'y' or 'n': ")
            if choose == "n":
                break
        return inserted_coins

    def check_txn_success(self, cost, inserted_coins):
        value = 0
        for toc, count in inserted_coins.items():
            value += self.coins_operated[toc] * count
        if cost > value:
            print("Sorry that's not enough money. Money refunded.")
            success = False
        else:
            remaining_change = value - cost
            if remaining_change > 0:
                print(
                    f"You have inserted coins more than the cost. Here is ${remaining_change} in change."
                )
            success = True
        return success

    def make_coffee(self, drink):
        # print(f"report before purchasing {drink}")
        # self.print_report()
        for ing, amt in drink["ingredients"].items():
            self.resources[ing] -= amt
        self.earnings += drink["cost"]
        # print(f"report after purchasing {drink}")
        # self.print_report()

    def start(self):
        while True:
            choice = self.make_front_panel_choice()
            drink = self.MENU[choice]
            if self.check_resources_for_drink(drink):
                inserted_coins = self.process_coins()
                if self.check_txn_success(drink["cost"], inserted_coins):
                    self.make_coffee(drink)
                    print(f"Here is your {choice} ☕, Enjoy!")


if __name__ == "__main__":
    CoffeeMachine().start()
