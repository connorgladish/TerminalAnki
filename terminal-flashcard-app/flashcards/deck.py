from .card import Card  # Import the Card class

class Deck:
    import json
    import random

    def __init__(self, deck_file):
        self.cards = []
        self.load_cards(deck_file)

    def load_cards(self, deck_file):
        with open(deck_file, 'r') as file:
            data = self.json.load(file)  # Use self.json to access the imported module
            for item in data['deck']:  # Fix to access the 'deck' key in JSON
                self.cards.append(Card(item['term'], item['definition']))

    def shuffle(self):
        self.random.shuffle(self.cards)

    def get_next_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None

class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def display(self):
        return f'Term: {self.term}\nDefinition: {self.definition}'

    def check_answer(self, answer):
        return answer.lower() == self.definition.lower()