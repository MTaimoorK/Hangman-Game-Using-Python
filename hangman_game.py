import random
from word_list import random_words

def get_words():
    word = random.choice(random_words)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    
    print("Let's Play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    
    while not guessed and tries > 0:
        guess = input("Please enter a letter or Word: ").upper()
        
        if len(guess) and guess.isalpha():
            if guess is guessed_letters:
                print("You already guessed this letter", guess)
                
            elif guess not in word:
                print(guess, "is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
                
            else:
                print("Great Work", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                
                for index in indices:
                    word_as_list[index] = guess
                
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word!", guess)
            
            elif guess != word:
                print(guess, "not in the word!")
                tries -= 1
                guessed_words.append(guess)
            
            else:
                guessed = True
                word_completion = word
            
        else:
            print ("Not a valid guess!")
        
        print(display_hangman(tries))
        print(word_completion)
        print("\n")        
    
    if guessed:
        print("Hurray! You have successfully guessed the word.")
    
    else:
        print("GAME OVER! You ran out of tries to guess the word. The hangman is dead!")    
      
def display_hangman(tries):
    stages = [
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]

    # Display the appropriate stage based on the number of incorrect guesses
    return stages[tries]

def main():
    word = get_words()
    play(word)
    
    while input ("Try Again?  (N/Y) ").upper() == "Y":
        word = get_words()
        play(word)
        
if __name__ == "__main__":
    main()
    