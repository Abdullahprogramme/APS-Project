# importing of libraries
import tkinter as tk
from tkinter import messagebox
import random
import numpy as np
from pygame import mixer
import math 

def Initializer(): # The initializer function which initializes all variables, constants and lists
    # declaration of any variable or lists used
    questions = []           # ''' empty 
    ActualQuestions = []     #     lists 
    BonusQuestions = []      #     for use '''
    state = {
        'score': 0, # score variable
        'Final': 1,                   # ''' answer sheet variable
        'Final_Text':  "Results:\n"   #     its text '''
    }
    num_to_words_list = random.sample(range(0, 27), 10) # random list of 10 numbers for decoding function
    distance_sum_list = random.sample(range(1, 11), random.randint(6, 7)) # random list of 6 or 7 in length for distance function
    factorial_val = random.choice([2, 6, 24, 120, 720, 5040, 40320]) # random number for factorial function
    matrix_list = [[random.randint(1, 10) for _ in range(3)] for _ in range(3)] # random 2d list for matrix
    find_powers_val = random.choice([4, 8, 9, 27, 36, 16, 81, 64]) # random number for power function
    base = random.randint(5, 15) # ''' base and height '''
    height = random.randint(3, 10) # ''' for geometery question '''
    a = random.randint(2, 5) # ''' three random constants
    b = random.randint(1, 20) #    for the algebra 
    c = random.randint(6, 10) #    question '''
    Length_lst = random.sample(range(5, 11), 2) # random list for Length question
    Prime_number = random.randint(3, 10) # random value for Prime question
    Fibonacci_number = random.randint(2, 10) # random value for Fibonacci question

    # questions list
    # contains all the questions and their functions in a dictionary
    text1 = "MATRIX MULTIPLICATION\n" + str(matrix_list) + " *" + "\n[[9, 8, 7], [6, 5, 4], [3, 2, 1]] is?\nEnter your answer in the form => x y z....."
    text2 = "Decode the following numbers into a word\n" + str(num_to_words_list) + "\nnumbers 1 to 26 represent a digit\n0 means space"
    text3 = "numbers = "  + str(distance_sum_list) + "\nIF ODD Lengthed, Find sum of absolute difference of each odd\nand even placed number except\nlast number and multiply with last number\nelse\nFind absolute difference of each odd placed\neven placed numbers"
    text4 = "Give the number whose factorial is " + str(factorial_val)
    text5 = "Write any combination of base and exponent\n for the number: " + str(find_powers_val) + " in format =>\n(base exponent)"
    text6  = f"Find the area of a triangle with\nbase {base} units and height {height} units.\nGive answer in floating point\nexample: 3.0 rounded to 1 decimal place"
    text7 = "I am a three-digit number.\n My tens digit is five more than my ones digit\n and hundreds digit is eight less\n than my tens digit What number am I?"
    text8  =f"Point 1 coordinates(2, {Length_lst[0]})\nPoint 2 coordinates(3, {Length_lst[1]})\n Find the distance between them\nexample: 3.0 rounded to 1 decimal place"
    text9 = f"Solve for x:\n{a}x + {b} = {c}\n Give answer in decimal number\nexample: 3.0 rounded to 1 decimal place"
    text10 = f"Provide a sequence of Fibonacci number\nto the {Fibonacci_number}th index in form => N x y z...\n0 and 1 are two starting numbers"
    text11 = "Enter a word which is palindrome, capitalized and odd in length"
    text12 = f"Enter all prime numbers below {Prime_number}\n in form => x y z... and so on"

    questions = [ # a list containing all the questions dictionaries with two keys.
        {'text': text12, 'check_answer': Prime},
        {'text': text1, 'check_answer': enumerated_matrix},
        {'text': text11, 'check_answer': PalinCapital},
        {'text': text10, 'check_answer': Fibonacci},
        {'text': text2, 'check_answer': numbers_to_words},
        {'text': text3, 'check_answer': distance_sum},
        {'text': text4, 'check_answer': find_factorial},
        {'text': text5, 'check_answer': find_powers},
        {'text': text6, 'check_answer': geometry_question},
        {'text': text9, 'check_answer': algebric_question},
        {'text': text7, 'check_answer': math_riddle},
        {'text': text8, 'check_answer': Length}
    ]

    # making a 5 question list to be used in the questionnaire out of a bigger pool
    for i in range(5):
        temp = random.choice(questions)
        ActualQuestions.append(temp)
        questions.remove(temp)

    # making a list of two question's functions which will get bonus try
    temp = random.sample(ActualQuestions, 2) # choosing two random questions
    for question in temp: # iterating in them to fetch the function name only
        BonusQuestions.append(question['check_answer'])

    return ActualQuestions, BonusQuestions, state, num_to_words_list, distance_sum_list \
            , factorial_val, matrix_list, find_powers_val, base, height, a, b, c, Length_lst, Prime_number, Fibonacci_number  

# loads a new question whenever provoked
def load_question(ActualQuestions, BonusQuestions, question_label, answer_entry, submit_button, state):
    global current_question, attempts_left
    if ActualQuestions: # check if questions left
        current_question = random.choice(ActualQuestions)
        if current_question["check_answer"] in BonusQuestions: attempts_left = 4 # if the question is a bonus one give an extra try
        else: attempts_left = 3 # else only three tries
        question_label.config(text=current_question['text']) # display the question on screen
        answer_entry.delete(0, tk.END)
        submit_button.config(state=tk.NORMAL)  # Enable the Submit button
    else: # else terminate loop
        messagebox.showinfo("Questionnaire Completed", "You have completed the questionnaire.")
        submit_button.config(state=tk.DISABLED)  # Disable the Submit button
        question_label.config(text=state['Final_Text'].strip())
        #root.quit()

# score updater function
def update_score(state, score_label):
    score_label.config(text=f"Current Score: {state['score']}")

# the music loader function
def music_loader(music_file): # takes a music file name and loads it and plays it
    mixer.music.load(music_file)
    mixer.music.play()

# evaluates the answer when the button is clicked
def evaluate_answer(ActualQuestions, BonusQuestions, num_to_words_list, distance_sum_list,  \
            factorial_val, matrix_list, find_powers_val, base, height, a, b, c, Length_lst, Prime_number, \
            Fibonacci_number, question_label, answer_entry, submit_button, score_label, state):
    global current_question, attempts_left

    try:
        answer = answer_entry.get()
        if current_question['check_answer'] == numbers_to_words:
            result = current_question['check_answer'](answer, num_to_words_list)
        elif current_question['check_answer'] == distance_sum:
            result = current_question['check_answer'](answer, distance_sum_list)
        elif current_question['check_answer'] == find_factorial:
            result = current_question['check_answer'](answer, factorial_val)
        elif current_question['check_answer'] == enumerated_matrix:
            result = current_question['check_answer'](answer, matrix_list)
        elif current_question['check_answer'] == find_powers:
            result = current_question['check_answer'](answer, find_powers_val)
        elif current_question['check_answer'] == geometry_question:
            result = current_question['check_answer'](answer, base, height)
        elif current_question['check_answer'] == algebric_question:
            result = current_question['check_answer'](answer, a, b, c)
        elif current_question['check_answer'] == Length:
            result = current_question['check_answer'](answer, Length_lst)
        elif current_question['check_answer'] == Prime:
            result = current_question['check_answer'](answer, Prime_number)
        elif current_question['check_answer'] == Fibonacci:
            result = current_question['check_answer'](answer, Fibonacci_number)
        else: result = current_question['check_answer'](answer)
        
        
        if result:
            music_loader("C:\Personal Files\OneDrive - Habib University\Python\APS Project files\correct-156911.mp3") # copy the path for this file on your pc
            messagebox.showinfo("Correct", "Your answer is correct!")
            ActualQuestions.remove(current_question)
            state['score'] += 1
            update_score(state, score_label)
            state['Final_Text'] += f"Question {state['Final']} was correct\n"
            state['Final'] += 1
            load_question(ActualQuestions, BonusQuestions, question_label, answer_entry, submit_button, state)
        else:
            attempts_left -= 1
            if attempts_left > 0:
                music_loader("C:\Personal Files\OneDrive - Habib University\Python\APS Project files\\failure-drum-sound-effect-2-7184.mp3") # copy the path for this file on your pc
                messagebox.showwarning("Incorrect", f"Your answer is incorrect. {attempts_left} attempts left.")
            else:
                music_loader("C:\Personal Files\OneDrive - Habib University\Python\APS Project files\\fiasco-154915.mp3") # copy the path for this file on your pc
                messagebox.showerror("Out of Attempts", "You have run out of attempts. Moving to the next question.")
                ActualQuestions.remove(current_question)
                state['Final_Text'] += f"Question {state['Final']} was incorrect\n"
                state['Final'] += 1
                load_question(ActualQuestions, BonusQuestions, question_label, answer_entry, submit_button, state)
            answer_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid data type. Please enter the correct data type.")
        answer_entry.delete(0, tk.END)

# Questions functions
def Prime(answer, Prime_number):
    try:
        numbers, N = list(answer.split(" ")), Prime_number
        if numbers == []: return False
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

    
def enumerated_matrix(answer, matrix_list):
    matrix_a = matrix_list

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
            
def Fibonacci(answer, Fibonacci_number):
    N = Fibonacci_number
    userList = [int(i) for i in answer.split(" ")] # making a list of all integers the user provided
    if Fibonacci_helper(N) == userList: return True # if comparision true 
    else: return False # if comparision false

def numbers_to_words(answer, num_to_words_list):
    n = num_to_words_list
    resul = ""
    for number in n:
        if number == 0:
            resul += " "  # space if the number is zero
        elif 1 <= number <= 26:
            resul += chr(ord('a') + number - 1)  # this line will convert to alphabet letter
    return resul == answer.lower()

def distance_sum(answer, distance_list):
    lst = distance_list
    n = len(lst) 
    if n % 2 == 1: # check for length to be odd
        last_element = lst[-1] # fetch last character
        n -= 1
    else:
        last_element = 1 # 1 in-case if length even
    
    distance_sum = 0
    for i in range(0, n, 2):
        distance_sum += abs(lst[i] - lst[i + 1]) # add absolute difference
    
    result = distance_sum * last_element
    return result == int(answer)

def find_factorial_helper(factorial_value, current = 1, factorial = 1):
    if factorial == factorial_value: # base case
        return current
    else:
        return find_factorial_helper(factorial_value, current + 1, factorial * (current + 1)) # recursive case

def find_factorial(answer, factorial_val):
    factorial_value = factorial_val
    return find_factorial_helper(factorial_value) == int(answer) # comparision

def find_powers(answer, number):
    b, e = map(int, answer.strip().split()) 
    power_representations = [] # List to store representations of the number as powers
    for base in range(2, int(number**0.5) + 1): # Iterate through possible bases
        exponent = 2
        # Check increasing exponents for each base
        while base**exponent <= number:
            if base**exponent == number: # If a representation is found, add it to the list
                power_representations.append((base, exponent))
            exponent += 1
    return (b, e) in power_representations

def geometry_question(answer, base, height):
    number = float(answer)
    correct_answer = 0.5 * base * height # Calculate area of the triangle
    return number == correct_answer # comparision

def algebric_question(answer, a ,b ,c):
    number = float(answer)
    correct_answer = (c - b) / a # solving for x
    return number == round(correct_answer, 1) # comparision

def math_riddle(answer): # sample answer list: [194, 285, 376, 467, 558, 649, 740, 831, 922]
    correct_answer = int(answer)
    lst = []
    for number in range(100, 1000):
        ones_digit = number % 10          # Extracting
        tens_digit = (number // 10) % 10  # the
        hundreds_digit = number // 100    # digits
        if tens_digit == ones_digit + 5 and hundreds_digit == tens_digit - 8: # Checking the conditions
            lst.append(number) # append to list if conditions are met True
    return correct_answer in lst # comparision

def Length(answer, Length_lst):
    distance = float(answer) # converting the answer to floating point
    y1, y2 = map(int, Length_lst) # mapping the y coordinates
    actual_distance = float(math.sqrt(math.pow(2 - 3, 2) + math.pow(y1 - y2, 2))) # finding the distance using math library
    return round(actual_distance, 1) == distance # comparision

# the Question functions end here
# ....................................................................................................................... #

# welcome message function
def show_welcome_message(ActualQuestions, BonusQuestions, question_label, root, answer_entry, submit_button, state):
    music_loader("C:\Personal Files\OneDrive - Habib University\Python\APS Project files\interface-welcome-131917.mp3") # copy the path for this file on your pc
    question_label.config(text="Welcome to the Python Questionnaire!")
    root.after(5000, lambda: load_question(ActualQuestions, BonusQuestions, question_label, answer_entry, submit_button, state))  # Schedule the load_question function after 5000 milliseconds (5 seconds)

def main():
    ActualQuestions, BonusQuestions, state,  num_to_words_list, distance_sum_list \
            , factorial_val, matrix_list, find_powers_val, base, height, a, b, c, Length_lst, Prime_number, Fibonacci_number = Initializer()
    
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

    question_label = tk.Label(question_frame, text="", font=("Helvetica", 12), fg="darkblue", bg="lightgreen")
    question_label.place(relwidth=1, relheight=1)

    # Answer Frame
    answer_frame = tk.Frame(main_frame, bg="orange", bd=5)
    answer_frame.place(relx=0.5, rely=0.6, relwidth=0.8, relheight=0.1, anchor="n")

    answer_entry = tk.Entry(answer_frame, bg="lightblue", fg="darkblue", font=("Helvetica", 12))
    answer_entry.place(relwidth=0.7, relheight=1)

    submit_button = tk.Button(answer_frame, text="Submit", command=lambda: evaluate_answer(ActualQuestions,\
            BonusQuestions, num_to_words_list, distance_sum_list,  \
            factorial_val, matrix_list, find_powers_val, base, height, a, b, c, Length_lst, Prime_number, \
            Fibonacci_number, question_label, answer_entry, submit_button, score_label, state), bg="gray", font=("Helvetica", 12))
    submit_button.place(relx=0.7, relwidth=0.3, relheight=1)

    mixer.init() # music initilizer

    # Load the initial question
    # first show the welcome message
    show_welcome_message(ActualQuestions, BonusQuestions, question_label, root, answer_entry, submit_button, state) # welcome message shower
    root.mainloop() # the main loop iterator

if __name__ == "__main__":
    main()
