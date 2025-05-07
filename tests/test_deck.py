import unittest
from flashcards.deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck('data/sample_deck.json')  # Pass the file path to Deck

    def test_load_cards(self):
        self.assertGreater(len(self.deck.cards), 0)

    def test_shuffle_deck(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_get_next_card(self):
        first_card = self.deck.get_next_card()
        self.assertIsNotNone(first_card)
        self.assertEqual(first_card.term, "Python")  # Match the first card in sample_deck.json

if __name__ == '__main__':
    unittest.main()