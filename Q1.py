def find_factorial(factorial_value, current, factorial):
    if current == factorial_value:
        return current
    else:
        return find_factorial(factorial_value, current + 1, factorial * (current + 1))

factorial_value = 24
result = find_factorial(factorial_value)
print(result)
