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
                if 'term' in item and 'definition' in item:
                    # Standard flashcard
                    self.cards.append(Card(item['term'], item['definition']))
                elif 'question' in item and 'options' in item:
                    # Multiple-choice card
                    question = item['question']
                    options = item['options']
                    correct_letter = item.get('answer')
                    correct_answer = options[correct_letter] if correct_letter in options else ""
                    self.cards.append(Card(question, correct_answer, options=options, answer=correct_letter, explanation=item.get('explanation')))

    def shuffle(self):
        self.random.shuffle(self.cards)

    def get_next_card(self):
        if self.cards:
            return self.cards.pop(0)
        return None

class Card:
    def __init__(self, term, definition, options=None, answer=None, explanation=None):
        self.term = term
        self.definition = definition
        self.options = options
        self.answer = answer
        self.explanation = explanation

    def display(self):
        if self.options:
            # Format the question with answer choices
            options_text = "\n".join([f"  {k}. {v}" for k, v in self.options.items()])
            return f"Question: {self.term}\nChoices:\n{options_text}"
        else:
            return f"Term: {self.term}\nDefinition: {self.definition}"

    def check_answer(self, answer):
        return answer.lower() == self.definition.lower()