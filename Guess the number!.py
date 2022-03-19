import random


game_active = True
print('welcome to my little game! I will think of a number of 1-10 and you have to guess it')
number_guess = input('but first, do you want to play?')
if number_guess == 'yes':
  print('lets play!')
if number_guess == 'no':
     quit()
number = random.randint(0,10)
print('Ok, I have thought of a number!')
number_guess = input('what do you think it is?: ')
if number_guess == number:
        play_again = input('Nice one! want to play again?')
        if play_again == 'no':
            quit()
        if play_again == 'yes':
            number_guess = input('what do you think it is?: ')
            if number_guess == number:
             play_again = input('Nice one! want to play again?')
             if play_again == 'yes':
                 game_active = True
             if play_again == 'no':
                 game_active = False
                 quit()
if number_guess == number + 1:
    print('you were close')
if number_guess == number - 1:
    print('you were close')

else: print('try again!')
while True:
    print('Ok, I have thought of a number!')
    number_guess = input('what do you think it is?: ')
    if number_guess == number:
      play_again = input('Nice one! want to play again?')
      if play_again == 'no':
            quit()
      if play_again == 'yes':
           while True:
            number_guess = input('what do you think it is?: ')
            if number_guess == number:
             play_again = input('Nice one! want to play again?')
             if play_again == 'yes':
                 game_active = True
             if play_again == 'no':
                 game_active = False
                 quit()
    else: print('try again!')
