def Question3():
    N = int(input("Enter a number you chose: "))
    number = input("Enter all prime factors within that number in format: xx yy zz and so on: " )
    numbers = list(number.split())
    new = []
    count = 2
    for i in range(2, N): # loop through 2 to N
        for j in range(2, i): # loop through 2 to that number in first loop
            if i % j == 0: count += 1
        if count <= 2: new.append(str(i)) # append if prime
        count = 2 # reset count
    if new == numbers: print("You are correct")
    else: print("You are incorrect")
