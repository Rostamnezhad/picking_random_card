
import random
cards = ["Diamonds", "Spades", "Hearts", "Clubs"]
ranks_of_cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "Q", "K"]

def pic_random_card():
    card = random.choices(cards)
    rank = random.choices(ranks_of_cards)
    return (f"The {rank} of {card}")

print(pic_random_card())
