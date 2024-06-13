"""Напишите программу которая содержит
список карт, умеет их перемешивать и позволяет
пользователю достать карту из колоды по ее
номеру. Всего в колоде 56 карт. Класс Card
содержит спискок номеров карт и список мастей."""
import random


class Card:
    """Represents a single playing card."""
    number_list = ['2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    mast_list = ['Hearts', 'Spades', 'Diamonds', 'Clubs']

    def __init__(self, number, mast):
        """Initializes a Card with a number and a mast (suit)."""
        self.number = number
        self.mast = mast

    def __str__(self):
        """Returns a string representation of the card."""
        return f'{self.mast} {self.number}'


class CardsDeck:
    """Represents a deck of playing cards including two jokers."""
    def __init__(self):
        """Initializes a CardsDeck including jokers."""
        self.cards = []
        for mast in Card.mast_list:
            for number in Card.number_list:
                self.cards.append(Card(number, mast))
        self.cards.append(Card('Black', 'Joker'))
        self.cards.append(Card('Red', 'Joker'))

    def shuffle(self):
        """Shuffles the deck of cards."""
        random.shuffle(self.cards)

    def get(self, index):
        """Returns the card at the specified index."""
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return False


deck = CardsDeck()
deck.shuffle()

while True:
    card_number = int(input('Choose a card from the 54-card deck (0-53): '))
    card = deck.get(card_number)
    if card:
        print(f'Your card is: {card}')
    else:
        print('Invalid card number. Please try again.')
