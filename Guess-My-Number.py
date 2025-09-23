import random

print('Welcome to the Number Guessing Game!')
print('I am thinking of a number between 0 and 20.')
random_number = random.randint(0, 21)
# print(random_number)
round_remaining = 10
score = 0
while round_remaining > 0:
    try:
        input_user = int(input('Choose a number: '))
    except ValueError:
        print('Please enter a valid number.')
        continue
    if input_user == random_number:
         if round_remaining > score:
             score += round_remaining
             print('You won the game!')
             print(f'Your score is: {score}')
             break
    else:
         if random_number > input_user:
             print("It's Higher ⬆️")
         elif input_user > random_number:
              print("It's Lower ⬇️")
         round_remaining -= 1
         print(f'You have {round_remaining} rounds remaining')
if round_remaining == 0:
    print('You have lost the game')
