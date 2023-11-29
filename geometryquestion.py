import random

def geometry_question():
    base = random.randint(5, 15)
    height = random.randint(3, 10)
    question = f"Find the area of a triangle with base {base} units and height {height} units."

    # Calculate area of the triangle
    correct_answer = 0.5 * base * height
    # Display the question
    print(question)
    return question, correct_answer

# Generate question and its correct answer
question, correct_answer = geometry_question()

#checking users answers
user_answer = float(input("Enter your answer: "))
if user_answer == correct_answer:
    print("Congratulations! Your answer is correct.")
else:
    #print(f"Sorry, the correct answer is {correct_answer}.")
