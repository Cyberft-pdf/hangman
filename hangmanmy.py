import time
import random
from words import words
import string 

print("-------------------------------------------------------------")
print(" ")
print("Hello, welcome to hangman game")
print(" ")
print("-------------------------------------------------------------")
time.sleep(3)
print(" ")
print("I'll write you commas. Each line represents a letter")
print(" ")
print("-------------------------------------------------------------")

time.sleep(6)
print(" ")
odpoved = input("Are you ready yes/no:")
print(" ")
print("-------------------------------------------------------------")

if odpoved == "yes":
    def get_valid_word(words):
        word = random.choice(words)
        while "-" in word or " " in word:
            word = random.choice(words)

        return word.upper()


    def hangman():
        word = get_valid_word(words)
        word_letters = set(word)
        alphabet = set(string.ascii_uppercase)
        used_letters = set()

        lives = 6
        while len(word_letters) > 0 and lives > 0:
            print("Remain :",lives, "lives you already used these letters: ", " ". join(used_letters))
            print(" ")
            word_list= [letter if letter in used_letters else "-" for letter in word] 
            print("The word you have now: "," ".join(word_list))
            print(" ")

            user_letter = input("Guess the letter:").upper()
            print(" ")
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives - 1 
                    print("The letter is not in the word.")
                    print(" ")

            elif user_letter in used_letters:
                print("You have already used this letter. Use another one")
                print(" ")

            else:
                print("Invalid character. Use another")
                print(" ")
        if lives == 0:
            print("Sorry, you lost :(", word)
        else:
            print("You guessed the right word", word, ":)")

    hangman()       
else:
    print("yes or no >:(")



if odpoved == "ne":
    print("so sorry :(")


        
