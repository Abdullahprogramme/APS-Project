# import tkinter as tk
# # create the main window
# window = tk.Tk()
# window.title("Random Questionnaire")


# def Question():
#     global tries
#     if tries == 1:
#         label.config(text="Enter a number you choose: ")
#         N = int(entry.get())
#     label.config(text="Enter all prime factors within that number in format: xx yy zz and so on: ")
#     number = entry.get()
#     numbers = list(number.split())
#     new = []
#     count = 2
#     for i in range(2, N): # loop through 2 to N
#         for j in range(2, i): # loop through 2 to that number in first loop
#             if i % j == 0: count += 1
#         if count <= 2: new.append(str(i)) # append if prime
#         count = 2 # reset count
#     if new == numbers:
#         showCorrect()
#     else:
#         ShowIncorrect()

# asas = {1: Question}

# def showCorrect():
#     result_label.config(text = "You are correct")

# def ShowIncorrect():
#     result_label.config(text = "You are Incorrect")



# #create a label 

# entry_var = tk.IntVar()

# label = tk.Label(window, text="", padx="100", pady="100")
# label.pack()

# entry = tk.Entry(window,textvariable=entry_var, width="50")
# entry.pack()

# button = tk.Button(window, text="Show", command=asas[1])
# button.pack()

# result_label = tk.Label(window, text="Result: ", padx=10, pady=10)
# result_label.pack()
# #start the main loop



# tries = 1
# flag = True
# while tries <= 4 and flag is True:
#     # if tries != 4:
#     #     tries, answer = asas[1]()
#     # if tries < 4:
#     #     if answer == "You are correct":
#     #         flag = False
#     #     print(answer)
#     if tries == 4 and flag is True: result_label.config(text="You failed")
#     tries += 1

# window.mainloop()

import tkinter as tk
from tkinter import messagebox
import random
import time


current_question = None
attempts_left = 3

def load_question():
    global current_question, attempts_left
    if asas:
        current_question = random.choice(asas)
        asas.remove(current_question)
        attempts_left = 3
        Pos_OR_Neg = current_question[1]()
        check_answer(Pos_OR_Neg)
        answer_entry.delete(0, tk.END)
    else:
        messagebox.showinfo("Questionnaire Completed", "You have completed the questionnaire.")
        root.destroy()

def Question():
    global attempts_left, value
    question_label.config(text="Enter a number 'a' in range(1 - 10) and\n enter all prime factors within that number\n in format: a xx yy zz and so on")

    try:
        number = value
        numbers = list(number.split())
        N, numbers = int(numbers[0]), numbers[1:]
        new = []
        count = 2
        for i in range(2, N): # loop through 2 to N
            for j in range(2, i): # loop through 2 to that number in first loop
                if i % j == 0: count += 1
            if count <= 2: new.append(str(i)) # append if prime
            count = 2 # reset count
        if new == numbers:
            return 1
        else:
            
            return -1
    except: return None
    
    

asas = [{1: Question}]

def Take_answer():
    global value
    value = answer_entry.get()

    
def check_answer(Pos_OR_Neg):
    global current_question, attempts_left
    
    try:
        if Pos_OR_Neg == None:
            current_question[1]()
        if Pos_OR_Neg == 1:
            messagebox.showinfo("Correct", "Your answer is correct!")
            load_question()
        else:
            attempts_left -= 1
            if attempts_left > 0:
                messagebox.showwarning("Incorrect", f"Your answer is incorrect. {attempts_left} attempts left.")
                current_question[1]()
            else:
                messagebox.showerror("Out of Attempts", "You have run out of attempts. Moving to the next question.")
                load_question()

    except ValueError:
        messagebox.showerror("Invalid Input", "Invalid data type. Please enter the correct data type.")
        answer_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Questionnaire App")
root.geometry("400x300")

question_label = tk.Label(root, text="", font=("Helvetica", 12))
question_label.pack(pady=20)

answer_entry = tk.Entry(root)
answer_entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=Take_answer)
submit_button.pack(pady=10)

load_question()

root.mainloop()
