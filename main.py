### Bulls and Cows game ###
import random
import time

print("Welcome to Bulls and Cows game"
      "\nB stands for number in correct place"
      "\nC stands for number in wrong place")

random_int = random.randint(11,99).__str__()
frandom = random_int[0]
srandom = random_int[1]

while True:
    guess_int = int(input('Guess a 2 digit number:'))
    if guess_int>99 or guess_int<10:
        guess_int = input('You need to guess a 2 digit number:')
    guess = guess_int.__str__()
    fguessed = guess[0]
    sguessed = guess[1]
    time.sleep(2)
    print(guess)
    #print(random_int)
    B=0
    C=0
    if fguessed==frandom and sguessed==srandom:
        break
    elif fguessed==frandom or sguessed==srandom:
        B=1
    elif fguessed==srandom and sguessed==frandom:
        C=2
    elif fguessed==srandom or sguessed==frandom:
        C=1
    print('B=',B,'C=',C)
print('Congratulations! You guessed right!')

