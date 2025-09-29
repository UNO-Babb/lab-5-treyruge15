#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    for ch in word:
        if letter == ch:
            return True
    return False

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    correctLetter = word[spot]
    if letter == correctLetter:
        return True
    return False

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""
    feedback = ""

    for spot in range(5):
        myLetter = myGuess[spot]
        if inSpot(myLetter, word, spot) == True:
            feedback = feedback + myLetter.upper() #denotes a correct letter location
        elif inWord(myLetter, word) == True:
            feedback = feedback + myLetter.lower() #denotes a correct letter
        else:
            feedback = feedback + "*"

    return feedback

def main():
    #Pick a random word from the list of all words
    wordFile = open("words.txt", 'r')
    content = wordFile.read()
    wordList = content.split("\n")
    todayWord = random.choice(wordList)
    

    #User should get 6 guesses to guess
    guessNum = 1
    while guessNum <= 6:
        #Ask user for their guess
        validWord = False
        while validWord == False:
            guess = input("Enter a guess for a 5 letter word: ")
            guess = guess.lower()
            if guess not in wordList:
                print("You spelled that wrong or you're making up words. Please enter a new word.")
                validWord = False
            else:
                validWord = True

        feedback = rateGuess(guess, todayWord)
        print(feedback)
        if feedback == todayWord.upper():
            print("Holy Smokes! You figured out the word in", guessNum, "tries!")
            break
        guessNum = guessNum + 1 
        #Give feedback using on their word:


    print("The word was", todayWord)
    print("Have a great day!")

if __name__ == '__main__':
  main()
