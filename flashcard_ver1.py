class Deck:
    def __init__(self, title, cards):
        self.title = title
        self.cards = cards

    def create_new_deck(self):
        decks.update({self.title: self.cards})


class Flashcards:
    def __init__(self, question, answer, time_taken):
        self.question = question
        self.answer = answer
        self.time_taken = time_taken


class Stats:
    def __init__(self, total_attempts, correct_attempts, deck_stats):
        self.total_attempts = total_attempts
        self.correct_attempts = correct_attempts
        self.deck_stats = deck_stats


decks = {
    "animal sounds": {"pig": "oink", "dog": "woof", "cat": "meow"}
         }
choice = 0
front = ""
mini_deck = {}
while True:
    while True:
        print("***************************")
        try:
            choice = int(input("Please enter function:\n1. Select deck\n2. Create new deck\n3. Exit\n: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        else:
            if 4 > choice > 0:
                break
            else:
                continue
    if choice == 3:
        print("Thanks for using the app!")
        exit()

    elif choice == 2:
        deck_name = input("Name of deck: ")
        while True:
            front = input("Text for front of card: (type 'Exit' to stop): ").title()
            if front == "Exit":
                break
            else:
                back = input("Text for back of card: ")
                mini_deck.update({front: back})
                deck1 = Deck(deck_name, mini_deck)
                deck1.create_new_deck()
        print(decks)
