country = "canada"
def hangman():
    wrong = 5
    guess = ""
    for i in range(len(country)):
        tryy = input("Guess the country letter by letter: ")

        if i < len(country) and tryy != country[i]:
            wrong -= 1
            print(f"Wrong. You are left with {wrong} tries")
        else:
            guess += tryy
            print(guess)
    
        if guess == country:
            print("Congratulations! You guessed it right !!.")
            return
        if wrong == 0:
            print(f"The correct country was {country}.")
            return
hangman()
