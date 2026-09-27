import random

fruits=['apple','mango','banana','pear','kiwi','papaya','guava','kiwi',
         'strawberry','plum','orange','mosambi','lemon','tomato','blueberry',
         'cassava','watermelon','physallis','grapefruit']

Your_guess={}
word=random.choice(fruits)
Secret_word=list(word)

for i in range(len(Secret_word)):
    Your_guess[i]='_'

print('You are playing Hangman.\nYou will have to guess a fruit\'s name within ten seconds.')
print('Otherwise the person will be hanged.')
print('Guess one letter at a time. For each wrong guess a second passes.')
print('Let\'s start')

for i in range(11):
    if i==10:
        print('Sorry. The person was hanged. You couldn\'t save him. The word was'+ word)
        break

    x=input()
    number=Secret_word.count(x)
    print('Your guess was in the word '+ str(number) +' times.')

    if number!=0:
        for j in range(len(Secret_word)):
            if Secret_word[j]==x:
                Your_guess[j]=x
        print('That letter was in the word')
        print(''.join(Your_guess.values()))
    
    else:
        print('That isn\'t in the word. Another second passes')

    if word==''.join(Your_guess.values()):
        print('You guessed the word! You saved the person!!')
        break
