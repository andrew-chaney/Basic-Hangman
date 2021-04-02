# Make a game of hangman to interact with the user
import random

def main():
    game_over = False

    wrong_count = 0

    word_list = ['firefighter', 'queen', 'juicy', 'banana', 'potato', 'monarchy', 'habitual', 'wallstreetbets']

    word = random.choice(word_list)

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    correct_letter_count = 0
    letter_count = []
    for i in range(len(word)):
        if word[i] not in letter_count:
            correct_letter_count += 1
            letter_count.append(word[i])

    used_letters = []
    correct_guesses = []

    while not game_over:
        board(wrong_count)
        display_word(word, correct_guesses)
        while True:
            try:
                user_choice = input("Enter a letter: ")
                choice_l = user_choice.lower()
                if (len(choice_l) > 1) or (choice_l not in alphabet):
                    raise Exception
                if choice_l in used_letters:
                    print(f"You've already guessed the letter '{choice_l}'.")
                elif choice_l in word:
                    used_letters.append(choice_l)
                    correct_guesses.append(choice_l)
                    break
                else:
                    print(f"'{choice_l}' is not in the word.")
                    used_letters.append(choice_l)
                    wrong_count += 1
                    break
                
            except Exception:
                print("ERROR: Incorrect input. Please only enter one letter.")
        if wrong_count == 6:
            board(wrong_count)
            print("Sorry, you lost! Better luck next time...")
            game_over = True
        elif correct_letter_count == len(correct_guesses):
            print("Congratulations, you won!")
            game_over = True
    
    print(f"The word was: {word}")
            

        

def display_word(word, correct):
    for l in word:
        if l in correct:
            print(l, end=" ")
        else:
            print("-", end=" ")
    print()

def board(count):
    board_dict[count]()

def gallows_start():
    print("     _____ ")
    print("     |   | ")
    print("     |     ")
    print("     |     ")
    print("     |     ")
    print("------------")

def head():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |     ")
    print("     |     ")
    print("------------")

def torso():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |   | ")
    print("     |     ")
    print("------------")

def arm1():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /| ")
    print("     |     ")
    print("------------")

def arm2():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\")
    print("     |     ")
    print("------------")

def leg1():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\")
    print("     |  /  ")
    print("------------")

def leg2():
    print("     _____ ")
    print("     |   | ")
    print("     |   O ")
    print("     |  /|\\ ")
    print("     |  / \\ ")
    print("------------")

board_dict = {
    0 : gallows_start,
    1 : head,
    2 : torso,
    3 : arm1,
    4 : arm2,
    5 : leg1,
    6 : leg2}


# Run main function
if __name__ == "__main__":
    main()