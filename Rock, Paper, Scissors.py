import random

print('You are playing Rock, Paper, Scissors!\nJust type in your choice without caps.')

moves=['rock','paper','scissors']
PP=0
CP=0

for i in range(10):
    player=input()
    computer=random.choice(moves)
    print('computer played '+computer)
    if player=='rock':
        if computer=='paper':
            CP+=1
        elif computer=='scissors':
            PP+=1
    elif player=='paper':
        if computer=='scissors':
            CP+=1
        elif computer=='rock':
            PP+=1
    elif player=='scissors':
        if computer=='rock':
            CP+=1
        elif computer=='paper':
            PP+=1
    print(PP,CP)
    if i==9:
        if PP>CP:
            print('YOU WIN!!!')
        elif PP==CP:
            print("IT'S A DRAW!")
        else:
            print('YOU LOSE :( Better luck next time!')