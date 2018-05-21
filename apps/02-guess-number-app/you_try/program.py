import random
print('---------------------------------')
print('     GUESS THE NUMBER APP        ')
print('---------------------------------')

number = random.randint(0, 100)
user_number = 10250

while int(user_number) != number:

    user_number = input('Guess a number between 0 and 100:')

    if number == int(user_number):
        print('YES! You\'ve got it. The number was '+str(number))
    elif int(user_number) > number:
        print('Sorry, but '+user_number+' is LOWER than the number')
    else:
        print('Sorry, but ' + user_number + ' is HIGHER than the number')
