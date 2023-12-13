secret_word = "ochieng"
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = input("Secret word: ")
    guess_count += 1

    if guess.upper() == 'OCHIENG':
        print("Congratulations, you have found the secret word!")
        break
    else:
        print("Sorry, you failed")
