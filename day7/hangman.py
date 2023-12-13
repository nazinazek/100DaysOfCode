
import random
import hangman_words
import hangnam_art

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6
display = []

for _ in range(word_length):
    display += "_"

print(hangnam_art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess in display:
        print(f"You've already guessed the letter {guess}")
    
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    if guess not in chosen_word:
        lives -=1
        print(hangnam_art.stages[lives])
        print(f"The letter {guess} not in the chosen word. You've losed a life!")
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(f"{' '.join(display)}")
        

    if "_" not in display:
        end_of_game = True
        print("You win.")

    