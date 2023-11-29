def math_riddle():
    for number in range(100, 1000):
        # Extracting digits
        ones_digit = number % 10
        tens_digit = (number // 10) % 10
        hundreds_digit = number // 100

        # Checking the conditions
        if tens_digit == ones_digit + 5 and hundreds_digit == tens_digit - 8:
            return number
# Display the riddle
print("I am a three-digit number.My tens digit is five more than my ones digit and hundreds digit is eight less than my tens digit What number am I?")

# User guess
userguess = int(input("Enter your three-digit number: "))

# Solve the riddle
correct_answer = math_riddle()
# Check user's answer
if userguess == correct_answer:
    print("Congratulations! Your answer is correct.")
#else:
    #print(f"Sorry, the correct answer is {correct_answer}.")

