import random
class Hangman:
    
    def __init__(self, word_list, num_lives=5):        
        self.random_index = random.randint(0, len(word_list) - 1)
        self.word = word_list[self.random_index]
        self.word_guessed = ["_"] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives 
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for i,letter in enumerate(self.word):
                if guess == letter:
                    self.word_guessed[i] = guess
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)

        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")


    def ask_for_input(self):
        while True:
            guess = input("Make a guess: ")
            if not guess.isalpha() or len(guess)!=1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(game.word_guessed)

    while True:
        if game.num_lives == 0:
            print("You lost")
            break
        elif game.num_letters != 0:
            game.ask_for_input() 
        else:
            print("Congratulations. You won the game!")
            break
        
play_game(word_list=["apple", "pear", "cherry", "kiwi", "orange", "mango"])