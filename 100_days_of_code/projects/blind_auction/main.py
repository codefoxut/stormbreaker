
import os

from projects.blind_auction.arts import logo


class BlindAuction:
    bids = {}

    @staticmethod
    def clear():
        os.environ.setdefault('TERM', 'xterm')
        cls = "cls" if os.name == 'nt' else "clear"
        os.system(cls)

    def start(self):
        self.bids = {}
        print(logo)
        print("Welcome to secret auction program!!")
        while True:
            name = input("what is your name? : ").lower()
            bid = float(input("What is your bid? : $"))

            self.bids[name] = bid

            cont = input("Are there any other bidders? Type 'yes' or 'no'\t")
            if cont.lower() == 'no':
                break
            else:
                self.clear()

        max_bid, person = 0, ''
        for p, b in self.bids.items():
            if b > max_bid:
                max_bid, person = b, p

        print(f"The winner is {person} with a bid of ${max_bid}")


if __name__ == '__main__':
    BlindAuction().start()
