country = "canada"
def hangman():
    hint = "starts with c"
    guess = ""
    print("Guess the country letter by letter")
    for i in range(len(country)):
        tryy = input("")

        if i < len(country) and tryy != country[i]:
            print(f"Wrong")
        else:
            guess += tryy
            print(f"guess: {guess}")
    
        if guess == country:
            print("Congratulations! You guessed it right !!.")
            return
hangman()
