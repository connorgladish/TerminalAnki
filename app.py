import os  # Add import for clearing the terminal
import json
from flashcards.deck import Deck

def create_new_deck():
    print("\nCreating a new study deck...")
    deck_name = input("Enter the name of the new deck: ").strip()
    deck_file = f"data/{deck_name}.json"
    new_deck = {"deck": []}

    while True:
        term = input("Enter a term (or type 'done' to finish): ").strip()
        if term.lower() == 'done':
            break
        definition = input(f"Enter the definition for '{term}': ").strip()
        new_deck["deck"].append({"term": term, "definition": definition})

    with open(deck_file, 'w') as file:
        json.dump(new_deck, file, indent=4)
    print(f"New deck saved as '{deck_file}'!")

def main():
    print(r"""
  _________  _______   ________  _____ ______   ___  ________   ________  ___          
 |\___   ___\\  ___ \ |\   __  \|\   _ \  _   \|\  \|\   ___  \|\   __  \|\  \         
 \|___ \  \_\ \   __/|\ \  \|\  \ \  \\\__\ \  \ \  \ \  \\ \  \ \  \|\  \ \  \        
      \ \  \ \ \  \_|/_\ \   _  _\ \  \\|__| \  \ \  \ \  \\ \  \ \   __  \ \  \       
       \ \  \ \ \  \_|\ \ \  \\  \\ \  \    \ \  \ \  \ \  \\ \  \ \  \ \  \ \  \____  
        \ \__\ \ \_______\ \__\\ _\\ \__\    \ \__\ \__\ \__\\ \__\ \__\ \__\ \_______\
         \|__|  \|_______|\|__|\|__|\|__|     \|__|\|__|\|__| \|__|\|__|\|__|\|_______|
                                                                                       
                                                                                       
                                                                                       
  ________  ________  ________  ________  ________  ___                                
 |\   ____\|\   __  \|\   __  \|\   ___ \|\   ____\|\  \                               
 \ \  \___|\ \  \|\  \ \  \|\  \ \  \_|\ \ \  \___|\ \  \                              
  \ \  \    \ \   __  \ \   _  _\ \  \ \\ \ \_____  \ \  \                             
   \ \  \____\ \  \ \  \ \  \\  \\ \  \_\\ \|____|\  \ \__\                            
    \ \_______\ \__\ \__\ \__\\ _\\ \_______\____\_\  \|__|                            
     \|_______|\|__|\|__|\|__|\|__|\|_______|\_________\  ___                          
                                            \|_________| |\__\                         
                                                         \|__|                         
    """)
    print("Welcome to Terminal Cards!")

    try:
        while True:
            print("\nMenu:")
            print("1. Study a deck")
            print("2. Create a new deck")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                deck_name = input("Enter the name of the deck to study (e.g., 'sample_deck'): ").strip()
                deck_file = f"data/{deck_name}.json"
                try:
                    deck = Deck(deck_file)
                    deck.shuffle()
                    correct = 0
                    total = 0
                    while True:
                        card = deck.get_next_card()
                        if not card:
                            break
                        if card.options:
                            # Multiple-choice card
                            print(f"\033[91mQuestion: {card.term}\033[0m")
                            options_text = "\n".join([f"  {k}. {v}" for k, v in card.options.items()])
                            print(f"Choices:\n{options_text}")
                            user_answer = input("\nEnter your answer (a/b/c/d): ").strip().lower()
                            correct_letter = card.answer
                            correct_text = card.options[correct_letter] if correct_letter in card.options else card.definition
                            if user_answer == correct_letter:
                                print(f"\033[92mCorrect!\033[0m")
                                correct += 1
                            else:
                                print(f"\033[91mIncorrect.\033[0m")
                                print(f"Correct answer: {correct_letter}. {correct_text}")
                            if card.explanation:
                                print(f"Explanation: {card.explanation}")
                            input("\nPress Enter to continue...")
                        else:
                            print(f"\033[91mTerm: {card.term}\033[0m")
                            input("\nPress Enter to see the definition...")
                            print(f"\033[94mDefinition: {card.definition}\033[0m")
                            while True:
                                result = input("\nDid you get it correct? (1 for Yes, 2 for No): ").strip()
                                if result == '1':
                                    correct += 1
                                    break
                                elif result == '2':
                                    break
                                else:
                                    print("Invalid input. Please enter 1 or 2.")
                        total += 1
                        os.system('cls' if os.name == 'nt' else 'clear')
                    print(f"\nYou got {correct} out of {total} correct.")
                    percentage = (correct / total) * 100
                    if percentage >= 80:
                        print("Congratulations! You passed!")
                    else:
                        print("Keep practicing! You can do it!")
                except FileNotFoundError:
                    print(f"Deck '{deck_name}' not found. Please create it first.")
            elif choice == '2':
                create_new_deck()
            elif choice == '3':
                print("\nExiting the application. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please try again.")
    except KeyboardInterrupt:
        print("\n\nExiting the application. Goodbye!")

if __name__ == "__main__":
    main()