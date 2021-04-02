# Make a game of hangman to interact with the user
import random

# Main loop function
def main():
    # Game hasn't been completed
    game_over = False
    # Tracks wrong guesses
    wrong_count = 0
    # Super basic word bank
    word_list = ['firefighter', 'queen', 'juicy', 'banana', 'potato', 'monarchy', 'habitual', 'wallstreetbets']
    # Chooses word to be guessed randomly from the word bank
    word = random.choice(word_list)
    
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Tracks how many letters need to be correctly guessed to be able to determine when the game is over
    correct_letter_count = 0
    letter_count = []
    # Iterate over the word to see how many correct guesses have to be made
    for i in range(len(word)):
        if word[i] not in letter_count:
            correct_letter_count += 1
            letter_count.append(word[i])
    # List of letters guessed and correct guesses
    # This will allow us to not double-jeopardy users for guessing the same wrong letter twice
    used_letters = []
    correct_guesses = []
    # While the game isn't over, keep playing
    while not game_over:
        # Display the right image that corresponds with the number of wrong guesses
        board(wrong_count)
        # Print the word with blanks for letters yet to be guessed
        display_word(word, correct_guesses)
        # Collect a guess from the user
        while True:
            # Get user input unless there's an error raised
            try:
                user_choice = input("Enter a letter: ")
                choice_l = user_choice.lower()
                # If the input is over 1 letter, or it isn't in the alphabet raise an error and don't accept
                if (len(choice_l) > 1) or (choice_l not in alphabet):
                    raise Exception
                # If they've already guessed that letter, don't accept
                if choice_l in used_letters:
                    print(f"You've already guessed the letter '{choice_l}'.")
                # If the letter is in the word, accept and update used letters and correct guesses lists
                elif choice_l in word:
                    used_letters.append(choice_l)
                    correct_guesses.append(choice_l)
                    break
                # If the guess is valid, but not in the word, accept and update the used letters list and wrong count
                else:
                    print(f"'{choice_l}' is not in the word.")
                    used_letters.append(choice_l)
                    wrong_count += 1
                    break
            # Error message for invalid input, do not break loop
            except Exception:
                print("ERROR: Incorrect input. Please only enter one letter.")
        # If the user exceeds allowed number of guesses, end the game and print answer
        if wrong_count == 6:
            board(wrong_count)
            print("Sorry, you lost! Better luck next time...")
            game_over = True
        # If the user guessed all of the right letters, end game and congratulate on victory.
        elif correct_letter_count == len(correct_guesses):
            print("Congratulations, you won!")
            game_over = True
    
    print(f"The word was: {word}")
            

        
# Function to print the word to be guessed with blanks for letters yet to be guessed correctly
def display_word(word, correct):
    for l in word:
        if l in correct:
            print(l, end=" ")
        else:
            print("-", end=" ")
    print()
    
# Print the board based on number of incorrect guesses
def board(count):
    board_dict[count]()
# No wrong guesses
def gallows_start():
    print("     _____ ")
    print("     |   | ")
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("------------")
# 1 wrong guess
def head():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |     ")
    print("     |     ")
    print("------------")
# 2 wrong guesses
def torso():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |   | ")
    print("     |     ")
    print("------------")
# 3 wrong guesses
def arm1():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /| ")
    print("     |     ")
    print("------------")
# 4 wrong guesses
def arm2():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\")
    print("     |     ")
    print("------------")
# 5 wrong guesses
def leg1():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\")
    print("     |  /  ")
    print("------------")
# 6 wrong guesses, game over!
def leg2():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\ ")
    print("     |  / \\ ")
    print("------------")
# Store board printouts as values and wrong guesses as keys for easier calling
board_dict = {
    0 : gallows_start,
    1 : head,
    2 : torso,
    3 : arm1,
    4 : arm2,
    5 : leg1,
    6 : leg2}


# Run the game
if __name__ == "__main__":
    main()
