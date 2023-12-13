
import random

import hangman_words
import hangnam_art

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
guessed = []
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(hangnam_art.logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess in guessed:
        print(f"You've already entered the letter {guess}")
    guessed.append(guess)

    if guess not in chosen_word:
        lives -=1
        print(hangnam_art.stages[lives])
        print(f"The letter {guess} not in the chosen word. Try again!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
        

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    