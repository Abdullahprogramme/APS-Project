import random

def generate_geometry_question():
    base = random.randint(5, 15)
    height = random.randint(3, 10)
    question = f"Find the area of a triangle with base {base} units and height {height} units."

    # Calculate area of the triangle
    correct_answer = 0.5 * base * height
    return question, correct_answer

# Generate question and its correct answer
question, correct_answer = generate_geometry_question()
# Display the question
#print(question)
# print(f"Correct Answer: {correct_answer}")
