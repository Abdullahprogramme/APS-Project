import tkinter as tk
from tkinter import messagebox
import random
import numpy as np

questions = []
ActualQuestions = []
score = 0

def load_question():
    global current_question, attempts_left
    if ActualQuestions:
        current_question = random.choice(ActualQuestions)
        attempts_left = 3
        question_label.config(text=current_question['text'])
        answer_entry.delete(0, tk.END)
        submit_button.config(state=tk.NORMAL)  # Enable the Submit button
    else:
        messagebox.showinfo("Questionnaire Completed", "You have completed the questionnaire.")
        submit_button.config(state=tk.DISABLED)  # Disable the Submit button
        #root.quit()

def update_score(score):
    score_label.config(text=f"Current Score: {score}")

def evaluate_answer():
    global current_question, attempts_left, score

    try:
        answer = answer_entry.get()
        result = current_question['check_answer'](answer)

        if result:
            messagebox.showinfo("Correct", "Your answer is correct!")
            ActualQuestions.remove(current_question)
            score += 1
            update_score(score)
            load_question()
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showwarning("Incorrect", f"Your answer is incorrect. {attempts_left} attempts left.")
            else:
                messagebox.showerror("Out of Attempts", "You have run out of attempts. Moving to the next question.")
                ActualQuestions.remove(current_question)
                load_question()
            answer_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid data type. Please enter the correct data type.")
        answer_entry.delete(0, tk.END)

# Questions functions
def Prime(answer):
    try:
        number = answer.strip()
        numbers = list(number.split())
        N, numbers = int(numbers[0]), numbers[1:]
        new = []
        count = 2
        for i in range(2, N):  # loop through 2 to N
            for j in range(2, i):  # loop through 2 to that number in the first loop
                if i % j == 0: count += 1
            if count <= 2: new.append(str(i))  # append if prime
            count = 2  # reset count
        return new == numbers
    except ValueError:
        return False
    
# def matrix(matrix_a, matrix_b, new_matrix):
#     for index_a, i in enumerate(matrix_a):
#         for index_b, j in enumerate(matrix_b):
#             new_matrix[index_a][index_b] = sum(i * j)
#     return new_matrix
def matrix(matrix_a, matrix_b, new_matrix):
    for index_a, row_a in enumerate(matrix_a):
        for index_b, row_b in enumerate(matrix_b.T):  # Transpose to get columns
            new_matrix[index_a][index_b] = sum(x * y for x, y in zip(row_a, row_b))
    return new_matrix

    
def enumerated_matrix(answer):
    matrix_a = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

    matrix_b = np.array([[9, 8, 7],
                      [6, 5, 4],
                      [3, 2, 1]])
  
    # enumerate method
    new_matrix = np.array([[0, 0, 0],
                        [0, 0, 0],
                        [0, 0, 0]])
  
    a1, a2, a3, b1, b2, b3, c1, c2, c3 = map(int, answer.strip().split())

    # Check if the user's answer matches the result of matrix multiplication
    return np.array_equal(matrix(matrix_a, matrix_b, new_matrix), [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]])

def Palindrome(N):
    if len(N) <= 1: # base case
        return True
    elif N[0] == N[-1]: # checks if first and last characters are same or not
        return Palindrome(N[1:-1]) # recursive case
    else: return False # base case

def Is_Length_Even(N):
    return False if (len(N) / 2 == 0) else True # returns True if the length is odd and returns False if it's even

def Cap_Or_NoCap(N):
    for i in N: # iterates in the string
        if ord(i) < 65 or ord(i) > 90: return False # checks if the character is not capital letter so returns False
    return True # if above statement fails it returns True

def PalinCapital(answer):
    N = answer.strip()
    if (Palindrome(N)) and (Is_Length_Even(N)) and (Cap_Or_NoCap(N)) is True: return True
    else: return False

def Fibonacci_helper(N):
        if N == 0: return [0] # base case where the index is 0
        elif N == 1: return [0, 1] # base case where the index is 1
        else: # general case where the index is > 1
            lst = Fibonacci_helper(N - 1) # keeps calling itself until it becomes 1
            lst.append(lst[-2] + lst[-1]) # appends the sum of last two numbers in lst
            return lst
            
def Fibonacci(answer):
    N = int(answer.strip()[0])
    userAnswer = answer[1:].strip()
    userList = [int(i) for i in userAnswer.split(" ")] # making a list of all integers the user provided
    if Fibonacci_helper(N) == userList: return True # if comparision true 
    else: return False # if comparision false

def numbers_to_words(answer):
    n = [1, 20, 8, 5, 0, 19, 9, 26, 30, -5]
    resul = ""
    for number in n:
        if number == 0:
            resul += " "  # space if the number is zero
        elif 1 <= number <= 26:
            resul += chr(ord('a') + number - 1)  # this line will convert to alphabet letter
        # else:
        #     if number < 0:
        #         result += "!"
        #     elif number > 26: 
        #         result += "?"  # We will Use! for negative and ? for if greater than 26
             
    return resul == answer

def distance_sum(answer):
    lst = [1,2,3,4]
    n = len(lst) 
    if n % 2 == 1:
        last_element = lst[-1]
        n -= 1
    else:
        last_element = 1
    
    distance_sum = 0
    for i in range(0, n, 2):
        distance_sum += abs(lst[i] - lst[i + 1])
    
    result = distance_sum * last_element
    return result == int(answer)

def find_factorial_helper(factorial_value, current = 1, factorial = 1):
    if factorial == factorial_value:
        return current
    else:
        return find_factorial_helper(factorial_value, current + 1, factorial * (current + 1))

def find_factorial(answer):
    factorial_value = 24
    return find_factorial_helper(factorial_value) == int(answer)
    
# the Question functions end here
# .......................................................................................................................

# questions list
# contains all the questions and their functions in a dictionary
questions = [
    {'text': "Enter a number 'a' in range(1 - 10) and\n enter all prime factors within that number\n in format: a xx yy zz and so on",
     'check_answer': Prime},
    {'text': '''  What is [[1, 2, 3]
                         [4, 5, 6]
                         [7, 8, 9]]
                            *
                        [[9, 8, 7]
                         [6, 5, 4]
                         [3, 2, 1]]
        Enter your answer here in the form xx yy zz.....''',
     'check_answer': enumerated_matrix},
    {'text': "Enter a word which is palindrome, capitalized and odd in length", 'check_answer': PalinCapital},
    {'text': "Enter a number 'N' in range (1 - 10) \n and provide it's sequence of Fibonacci number \n to the Nth index in form xx yy zz....",
     'check_answer': Fibonacci},
    {'text': "Decode the following numbers into a word\n[1, 20, 8, 5, 0, 19, 9, 26]\nnumbers 1 to 26 represent a digit", 'check_answer': numbers_to_words},
    {'text': "IF ODD Lengthed, Find sum of absolute difference of all odd\nplaced numbers and even placed numbers\nand multiply with last number\nelse\nFind absolute difference of all odd placed\nnumbers and even placed numbers. numbers = [1,2,3,4]", 'check_answer': distance_sum},
    {'text': "Give the number which's factorial 24 is", 'check_answer': find_factorial}
]
# making a 5 question list to be used in the questionnaire out of a bigger pool
for i in range(5):
    temp = random.choice(questions)
    ActualQuestions.append(temp)
    questions.remove(temp)
print(len(ActualQuestions))
def show_welcome_message():
    question_label.config(text="Welcome to the Python Questionnaire!")
    root.after(10000, clear_welcome_message)  # Schedule the clear_welcome_message function after 5000 milliseconds (5 seconds)

def clear_welcome_message():
    question_label.config(text="")  # Clear the label text

# GUI initialization
root = tk.Tk()
root.title("Questionnaire App")
root.geometry("600x450")
root.configure(bg="lightgray")

# Main Frame
main_frame = tk.Frame(root, bg="lightgray")
main_frame.pack(expand=True, fill="both")

# Score Frame
score_frame = tk.Frame(main_frame, bg="purple", bd=5)
score_frame.place(relx=0.5, rely=0, relwidth=0.8, relheight=0.1, anchor="n")

score_label = tk.Label(score_frame, text="Current Score: 0", font=("Helvetica", 12), bg="lightgreen")
score_label.place(relwidth=1, relheight=1)

# Question Frame
question_frame = tk.Frame(main_frame, bg="teal", bd=5)
question_frame.place(relx=0.5, rely=0.15, relwidth=0.8, relheight=0.4, anchor="n")

question_label = tk.Label(question_frame, text="", font=("Helvetica", 12), bg="lightgreen")
question_label.place(relwidth=1, relheight=1)

# Answer Frame
answer_frame = tk.Frame(main_frame, bg="orange", bd=5)
answer_frame.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.1, anchor="n")

answer_entry = tk.Entry(answer_frame, bg="lightblue", font=("Helvetica", 12))
answer_entry.place(relwidth=0.7, relheight=1)

submit_button = tk.Button(answer_frame, text="Submit", command=evaluate_answer, bg="gray", font=("Helvetica", 12))
submit_button.place(relx=0.7, relwidth=0.3, relheight=1)

# Load the initial question
#show_welcome_message()
load_question()

root.mainloop()
