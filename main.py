import random
from random import randint

print(f"\nPreparing...\n")

def main():


    print(f"Running game setup...\n")


    class game_setup():

        ans = random.randint(1, 9)
        strike = 0

        def __init__(self, ans, strike):

            self.ans = ans
            self.strike = strike


    ans = game_setup.ans
    strike = game_setup.strike

    print(f"Setup complete!\n")


    while True:


        if 3 - strike != 1:
            
            guess = input(f"Can you guess the number between 1 and 10, inclusive? You have {3 - strike} attempts left.\n\n")
        
        elif 3 - strike == 1:

            guess = input(f"Can you guess the number between 1 and 10, inclusive? You have {3 - strike} attempt left.\n\n")


        if int(guess) == ans:

            try:

                if strike + 1 == 1:

                    print(f"\n\n")
                    print(f"You got it! The answer was {ans}! You got it in {strike + 1} try!")
                    print(f"\n\n\n")

                else:

                    print(f"\n\n")
                    print(f"You got it! The answer was {ans}! You got it in {strike + 1} tries!")
                    print(f"\n\n\n")

            finally:

                break


        else:

            try:

                if int(guess) > ans:

                    print(f"\n\n")
                    print(f"Strike {strike + 1}")
                    print(f"\n")
                    print(f"Lower")
                    print(f"\n\n\n")


                elif int(guess) < ans:
                    
                    print(f"\n\n")
                    print(f"Strike {strike + 1}")
                    print(f"\n")
                    print(f"Higher")
                    print(f"\n\n\n")

            finally:

                strike = strike + 1


        if strike > 2:

            print(f"\n\n")
            print(f"That\'s your third strike!")
            print(f"\n")
            print(f"The answer was {ans}, better luck next time...")
            print(f"\n\n\n")

            break



main()
