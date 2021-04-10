import math

from alphabets import alphabet


# Define a function called paint_calc() so that the code below works.
def paint_calc(height, width, cover):
    # Write your code below this line 👇
    nr_cans = (height * width) / cover
    # Write your code above this line 👆
    print(int(math.ceil(nr_cans)))


def paint_wall():
    # 🚨 Don't change the code below 👇
    test_h = int(input("Height of wall: "))
    test_w = int(input("Width of wall: "))
    coverage = 5
    paint_calc(height=test_h, width=test_w, cover=coverage)


def prime_checker(number):
    # Write your code below this line 👇
    div = number // 2
    is_prime = True
    for i in range(2, div, 2):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
    # Write your code above this line 👆


def check_prime_number():
    # Do NOT change any of the code below👇
    n = int(input("Check this number: "))
    prime_checker(number=n)


class CaesarPractice:
    def _encrypt(self, plain_text, shift_amount):
        # TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

        # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
        #         amount and print the encrypted text.
        # e.g.
        # plain_text = "hello"
        # shift = 5
        # cipher_text = "mjqqt"
        # print output: "The encoded text is mjqqt"

        # #HINT: How do you get the index of an item in a list:
        # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        # #🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
        alpha_len = len(alphabet)
        cipher_text = ""
        for i in plain_text:
            if i in alphabet:
                index = alphabet.index(i)
                new_index = (index + shift_amount) % alpha_len
                cipher_text += alphabet[new_index]
            else:
                cipher_text += i
        print(f"The encoded text is {cipher_text}")

    def _decrypt(self, cipher_text, shift_amount):

        # TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

        # TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet
        #         by the shift amount and print the decrypted text.
        # e.g.
        # cipher_text = "mjqqt"
        # shift = 5
        # plain_text = "hello"
        # print output: "The decoded text is hello"

        alpha_len = len(alphabet)
        plain_text = ""
        for i in cipher_text:
            if i in alphabet:
                index = alphabet.index(i)
                new_index = (index - shift_amount) % alpha_len
                plain_text += alphabet[new_index]
            else:
                plain_text += i
        print(f"The decoded text is {plain_text}")

    def caesar(self, start_text, shift_amount, cipher_direction):
        # TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
        alpha_len = len(alphabet)
        end_text = ""
        resp_type = "encoded" if cipher_direction == "encode" else "decoded"
        shift_amount = (
            shift_amount * -1 if cipher_direction == "decode" else shift_amount
        )
        for i in start_text:
            if i in alphabet:
                index = alphabet.index(i)
                new_index = (index + shift_amount) % alpha_len
                end_text += alphabet[new_index]
            else:
                end_text += i
        print(f"The {resp_type} text is {end_text}")

    def step_1(self):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and
        #         encrypt a message.
        self._encrypt(plain_text=text, shift_amount=shift)

    def step_2(self):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable.
        #         Then call the correct function based on that 'direction' variable.
        #         You should be able to test the code to encrypt *AND* decrypt a message.
        if direction == "encode":
            self._encrypt(plain_text=text, shift_amount=shift)
        else:
            self._decrypt(cipher_text=text, shift_amount=shift)

    def step_3(self):
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        # TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
        self.caesar(start_text=text, shift_amount=shift, cipher_direction=direction)


if __name__ == "__main__":
    # paint_wall()
    # check_prime_number()
    # CaesarPractice().step_1()
    # CaesarPractice().step_2()
    CaesarPractice().step_3()
