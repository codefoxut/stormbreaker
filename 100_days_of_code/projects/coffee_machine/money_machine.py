class MoneyMachine:
    CURRENCY = "$"
    coins_operated = {"quarters": 0.25, "dimes": 0.10, "nickles": 0.05, "pennies": 0.01}

    def __init__(self, money):
        self.earnings = money
        self.inserted_coins = {}

    def report(self):
        print(f"Money: {self.CURRENCY}{self.earnings}")

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
                    f"You have inserted coins more than the cost. Here is {self.CURRENCY}{remaining_change} in change."
                )
            success = True
        return success

    def make_payment(self, cost: float):
        inserted_coins = self.process_coins()
        return self.check_txn_success(cost, inserted_coins)
