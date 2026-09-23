import random

def get_guess():
    number=input("Guess number between 1 and 100: ")
    return number

number=random.randint(1, 100)
attempt=0
remaining=0
while True:
    guess=int(get_guess())
    attempt += 1 
    remaining = 7-attempt
    #print(number)
    if number==guess:
        print("Correct")
        print(f"You got it in {attempt} attempts.")
        break
    elif attempt==7:
        print("Game over!")
        print(f"The number was {guess}")
        break
    elif number > guess:
        print("it is too low")
        print(f"You have {remaining} attempts remainng.")
    else:
        print("it is too high")
        print(f"You have {remaining} attempts remainng.")
        

