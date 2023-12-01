def find_powers(number):
    # Check for invalid input
    if number <= 0:
        return "Invalid input. Please provide a positive integer."

    # List to store representations of the number as powers
    power_representations = []

    # Iterate through possible bases
    for base in range(2, int(number**0.5) + 1):
        exponent = 2

        # Check increasing exponents for each base
        while base**exponent <= number:
            # If a representation is found, add it to the list
            if base**exponent == number:
                power_representations.append((base, exponent))
            exponent += 1

    if not power_representations:
        return str(number) + " is not a perfect power."

    return str(number) + " can be represented as powers: " + str(power_representations)
print(find_powers(number))
