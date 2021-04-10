from projects.calculator1.arts import logo


class Calculator1:

    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def subtract(n1, n2):
        return n1 - n2

    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

    @staticmethod
    def divide(n1, n2):
        return n1 / n2


    def start(self):
        print(logo)
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

        new_calculation = True
        first_number = 0
        while True:
            if new_calculation:
                first_number = float(input("What's the first number? \t"))

            for key in operations:
                print(key)

            while True:
                func_str = input("Pick an operation:\t").strip()
                func = operations.get(func_str, None)
                if func:
                    break

            second_number = float(input("What's the next number? \t"))
            answer = func(first_number, second_number)
            print(f"{first_number} {func_str} {second_number} = {answer}")
            cont = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation "
                         f"or type 'c' to exit: \n")
            if cont == 'y':
                first_number = answer
                new_calculation = False
            elif cont == 'n':
                new_calculation = True
            else:
                break


if __name__ == '__main__':
    Calculator1().start()
