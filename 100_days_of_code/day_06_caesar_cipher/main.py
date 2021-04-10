from arts import logo
from alphabets import alphabet


class CaesarCipher:
    def caesar(self, start_text, shift_amount, cipher_direction):
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
        print(f"Here's the {resp_type} text: {end_text}")

    def start(self):
        # TODO-1: Import and print the logo from art.py when the program starts.
        print(logo)
        # TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
        # e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
        # If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
        # Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
        while True:
            cnt_program = input(
                "Do you want to restart the cipher program? Type yes or no\n"
            )

            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))

            # TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
            # Try running the program and entering a shift number of 45.
            # Add some code so that the program continues to work even
            # if the user enters a shift number greater than 26.
            # Hint: Think about how you can use the modulus (%).
            shift = shift % len(alphabet)

            self.caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

            if cnt_program == "no":
                print("GoodBye")
                break


if __name__ == "__main__":
    CaesarCipher().start()
