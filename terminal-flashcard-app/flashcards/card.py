class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def display(self):
        print(f"Term: {self.term}")
        print(f"Definition: {self.definition}")

    def check_answer(self, answer):
        return answer.strip().lower() == self.definition.strip().lower()