import random as r
lower = 0
higher = 10
answer = r.randint(lower,higher)
print("Please guess number between {} to {}: ".format(lower,higher))
guess_no = int(input())
if guess_no == answer:
    print("Congrat's you did it in first go")
else:
    if guess_no < answer:
        print("Have one more try, you guessed higher")
    else:
        print("Have one more try, you guessed lower")
    guess_no = int(input())
    if guess_no == answer:
        print("Well done you guessed it correct!")
    else:
        print("Sorry! You lose")
        print("Correct answer was {}".format(answer))
