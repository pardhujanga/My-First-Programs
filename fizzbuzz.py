for i in range(1,101):#in a loop, continue will skip to the next iteration of the loop and end the current one.
    x=''
    if i%3==0:
        x+='fizz'
    if i%5==0:
        x+='buzz'
    if x!='':
        print(x)
    else:
        print(i)
