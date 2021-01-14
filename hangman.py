"""
Need a list to hold all possible word choices.
Need a list to hold all letter choices from the user.
Need a variable to hold current wrong_letter count
Need a function to choose a random word from the word bank

When random word is chosen need to create a list with "_"
in place of the letters of each word.

Need input to take the user's guess. Input needs to conver
to UPPER CASE.
Input needs to filter out all other data types.
Input needs to accept only single string/char
Input cannot be a previously guessed letter.

After user enters current letter:
Function to compare current letter with current word
    IF letter is not in current word
    Increase wrong_letter count by 1
    ELSE letter is in current word
    Replace "_" with letter. Use index for letter

"""

word_bank = ["TRIPE", "KINDLE", "MOUSEPAD", "KALEIDOSCOPE"]
current_word = []
guessed_letters = []
wrong_guesses_remaining = 6

def random_word():
    # select a random number between 0 and length of word_bank
    # current_word = word_bank[index location chosen]
    return 

def guess_letter():
    print("Guess a letter")
    user_letter = input(" ")
    return user_letter

