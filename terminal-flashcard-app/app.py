# filepath: terminal-flashcard-app/terminal-flashcard-app/app.py

from flashcards.deck import Deck

def main():
    print("Welcome to the Terminal Flashcard App!")
    deck = Deck('data/sample_deck.json')  # Pass the file path to Deck

    while True:
        print("\nSelect a study deck:")
        print("1. Sample Deck")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            deck.shuffle()
            while True:
                card = deck.get_next_card()
                if not card:
                    print("You have completed the deck!")
                    break
                print(f"\nTerm: {card.term}")
                input("Press Enter to see the definition...")
                print(f"Definition: {card.definition}")
                input("Press Enter for the next card...")
        elif choice == '2':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()