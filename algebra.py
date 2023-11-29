import random
def algebraic_question():
    # Generate random values for the equation ax + b = c
    a = random.randint(2, 5)
    b = random.randint(1, 20)
    x = random.randint(6, 10)
    c = a * x + b

    question = f"Solve for x: {a}x + {b} = {c}"
    answer = (c - b) / a
    return question, answer
    
# Generate question and its answer
question, answer = algebraic_question()
# Display the question
print(question)
your_answer = int(input("Enter your answer: "))

# Check user's answer
if your_answer == answer:
    print("Congratulations! Your answer is correct.")
else:
    print(f"Sorry, the correct answer is {answer}. Try again next time.")
