print('Number guessing game')
number=9
hello=int( input('enter your number: '))
if hello == number :
        print('you guessed the correct number')

elif hello < number:
        print('Guess a greater number')

else:
        print('Guess a smaller number')

