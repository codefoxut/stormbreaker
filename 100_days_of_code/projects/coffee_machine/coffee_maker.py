from projects.coffee_machine.menu import MenuItem


class CoffeeMaker:
    def __init__(self, water, milk, coffee):
        self.resources = {"water": water, "milk": milk, "coffee": coffee}

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink: MenuItem):
        success = True
        for ingredient, quantity in drink.ingredients.items():
            if self.resources[ingredient] < quantity:
                print(f"Sorry there is not enough {ingredient}.")
                success = False
                break
        return success

    def make_coffee(self, order: MenuItem):
        for ingredient, quantity in order.ingredients.items():
            self.resources[ingredient] -= quantity
        print(f"Here is your {order.name} ☕️. Enjoy!")
