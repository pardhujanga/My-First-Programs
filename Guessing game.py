import random

number=random.randrange(1,11)
name=input("Hello, what's your name?")

print('Okay '+name+', I am going to choose a number. You have to guess it within 5 tries.')

for i in range(5):
    guess=int(input())
    if i==4 and guess!=number:
        print('you lost')
    else:
        if guess==number:
            print("That's right")
            print('your score is '+str(5-i))
            break
        elif guess>number:
            print('Lower')
        else:
            print('higher')
