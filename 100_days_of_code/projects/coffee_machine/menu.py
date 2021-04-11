class MenuItem:
    def __init__(self, name, cost, ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients


class Menu:
    def __init__(self):
        self.menu = {
            "espresso": MenuItem(
                "espresso",
                cost=1.5,
                ingredients={
                    "water": 50,
                    "coffee": 18,
                },
            ),
            "latte": MenuItem(
                "latte",
                cost=2.5,
                ingredients={
                    "water": 200,
                    "milk": 150,
                    "coffee": 24,
                },
            ),
            "cappuccino": MenuItem(
                "cappuccino",
                cost=3.0,
                ingredients={
                    "water": 250,
                    "milk": 100,
                    "coffee": 24,
                },
            ),
        }

    def get_items(self):
        return "/".join(k for k in self.menu)

    def find_drink(self, order_name):
        obj = self.menu.get(order_name)
        if not obj:
            print("Sorry that item is not available.")
        return obj
