asas = {1: Question}
tries = 1
flag = True
while tries <= 4 and flag is True:
    if tries != 4:
        tries, answer = asas[1]()
    if tries < 4:
        print(answer)
    elif tries == 4 and flag is True: print("You failed")
    tries += 1
