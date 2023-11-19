#This is a question where the user will be given a number and will need to simply decode a long list of numbers
#into a string. The index 1 is for a, and so on up to 26 alphabets, but if the number is greater than 26, it will be a! sign, and? if it is less than 0. Zero will be a space

def numbers_to_words(n):
    result = ""
    for number in n:
        if number == 0:
            result += " "  # space if the number is zero
        elif 1 <= number <= 26:
            result += chr(ord('a') + number - 1)  # this line will convert to alphabet letter
        else:
            if number < 0:
                result += "!"
            elif number > 26: 
                result += "?"  # We will Use! for negative and ? for if greater than 26
             
    return result

print(numbers_to_words([1, 20, 8, 5, 0, 19, 9, 26, 30, -5]))
