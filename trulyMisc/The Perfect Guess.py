print("********** The Perfect Guess **********\n")

low = int(input("Enter the lower limit: "))
up = int(input("Enter the upper limit: "))

def start():
    num_user = int(input("\nGuess the number: "))
    return num_user


l = []

import random
num = random.randint(low,up)

for i in range(low,up+1):
    num_user = start()
    if num_user > num:
        l.append(num_user)
        print("Lower number please!")
        print(f"Numbers you have already guessed: {l}")
    elif num_user < num:
        l.append(num_user)
        print("Higher number please!")
        print(f"Numbers you have already guessed: {l}")
    elif num == num_user:
        print("Congratulations! You have guessed the number.")
        break
    else:
        pass

print(f"You arrived at the number after {len(l)+1} guesses.")