import random

def guess(key, guess):
    while guess != key:
            if guess < key:
                print("Guess a little higer...")
                guess = int(input("Guess a 3-digit number: "))
            elif guess > key:
                print("Guess a little lower...")
                guess = int(input("Guess a 3-digit number: "))
    if guess == key:
        print("Correct!")

def main():
    # create three random digits for a 3-digit key
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    c = random.randint(1, 9)

    # ask player for a guess
    guess1 = int(input("Guess the first digit: "))
    guess(a, guess1)
    guess2 = int(input("Guess the second digit: "))
    guess(b, guess2)
    guess3 = int(input("Guess the third digit: "))
    guess(c, guess3)

    print("The key was {}{}{}".format(a, b, c))
 

main()