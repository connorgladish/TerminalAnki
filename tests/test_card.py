import unittest
from flashcards.card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card(term="Python", definition="A programming language.")

    def test_display(self):
        self.assertEqual(self.card.display(), "Term: Python\nDefinition: A programming language.")

    def test_check_answer_correct(self):
        self.assertTrue(self.card.check_answer("A programming language."))

    def test_check_answer_incorrect(self):
        self.assertFalse(self.card.check_answer("Incorrect definition."))

if __name__ == '__main__':
    unittest.main()