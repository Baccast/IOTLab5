import sys

# List to store words
words = []


# Get words from user
def get_words():
    while True:
        try:
            # Get user input
            user_input = input("\nEnter a word (or type 'show' to display all words): ")
        except KeyboardInterrupt:
            sys.exit("\nProgram cancelled by user.\n")
        # Check if user wants to display all words
        if user_input.lower() == "show":
            print("Words entered so far: ", words)
            ask_to_continue()
        # Check if user input is a word
        elif user_input.isalpha():
            # Check if word already exists
            if user_input in words:
                print("The value already exists.")
            # Add word to list
            else:
                words.append(user_input)
                print("New value registered.")
        # Check if user input is invalid
        else:
            print("Invalid input. Please enter a word with only alphabetic characters.")


# Ask user if they want to continue entering words
def ask_to_continue():
    while True:
        try:
            # Get user input
            user_input = input("\nDo you want to continue entering words? (Y/N): ")
        except KeyboardInterrupt:
            sys.exit("\nProgram cancelled by user.\n")

        # Check if user wants to continue
        if user_input.lower() == "y":
            get_words()
        # Check if user wants to exit
        elif user_input.lower() == "n":
            sys.exit("\nExiting program. Goodbye!\n")
        # Check if user input is invalid
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")


if __name__ == "__main__":
    get_words()
