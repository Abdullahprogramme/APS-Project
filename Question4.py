def Fibonacci():
    N = int(input("Enter a number in range 1-10: "))
    userAnswer = input("Now produce a squence of Fibonacci number to the Nth index in form xx yy zz....: ")
    userList = [int(i) for i in userAnswer.split(" ")] # making a list of all integers the user provided
    def Fibonacci_helper(N):
        if N == 0: return [0] # base case where the index is 0
        elif N == 1: return [0, 1] # base case where the index is 1
        else: # general case where the index is > 1
            lst = Fibonacci_helper(N - 1) # keeps calling itself until it becomes 1
            lst.append(lst[-2] + lst[-1]) # appends the sum of last two numbers in lst
            return lst
        
    if Fibonacci_helper(N) == userList: print("Your answer is correct") # if comparision true 
    else: print("Your answer is incorrect") # if comparision false
Fibonacci()
