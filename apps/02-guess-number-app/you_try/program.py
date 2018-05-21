import random
print('---------------------------------')
print('     GUESS THE NUMBER APP        ')
print('---------------------------------')

number = random.randint(0, 100)
user_number = 10250

while user_number != number:

    user_number = int(input('Guess a number between 0 and 100:'))

    if user_number == number:
        print('YES! You\'ve got it. The number was {}'.format(number))
    elif user_number > number:
        print('Sorry, but {} is HIGHER than the number'.format(user_number))
    else:
        print('Sorry, but {} is LOWER than the number'.format(user_number))
