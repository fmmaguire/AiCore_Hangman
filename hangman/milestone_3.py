import random

word_list = ["apple", "banana", "cherry", "orange", "grape", "kiwi"]
random_index = random.randint(0, len(word_list) - 1)
word = word_list[random_index]
print(word)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    print("Make a guess!")
    while True:
        guess = input()
        if guess.isalpha() & len(guess)==1:
            print("Accepted!")
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

ask_for_input()


