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

    def get_value(self):
        """Returns the numeric value of the card."""
        if self.number.isdigit():
            return int(self.number)
        if self.number in ['J', 'Q', 'K']:
            return 10
        if self.number == 'A':
            return 11  # For simplicity, assuming Ace always equals 11
        return 0  # Return 0 for jokers or invalid cards


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
        return self.cards[index]


deck = CardsDeck()
deck.shuffle()

while True:
    card_number = int(input('Choose a card from the 54-card deck (0-53): '))
    if 0 <= card_number < len(deck.cards):
        card = deck.get(card_number)
        print(f'Your card is: {card}')
        print(f'Card value: {card.get_value()}')
    else:
        print('Invalid card number. Please try again.')
