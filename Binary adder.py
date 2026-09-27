x='1010011'
y='1010' #this took me a long time to make, but was very satisfying in the end
z=''
c='0'
n=len(x)

while len(x)!=len(y):
    if len(x)>len(y):
        y='0'+y
    elif len(x)<len(y):
        x='0'+x

for i in range(n):
    if i>0:
        if x[n-i]=='0' and z[0]=='1':
            c='0'
        elif y[n-i]=='0' and z[0]=='1':
            c='0'
        elif x[n-i]=='0' and y[n-i]=='0' and z[0]=='0':
            c='0'
        else:
            c='1'

    if int(x[n-i-1])+int(y[n-i-1])+int(c)==2 or int(x[n-i-1])+int(y[n-i-1])+int(c)==0:
        z='0'+z
    else:
        z='1'+z

if (int(x[0]) and int(y[0]))==0 and z[0]=='1':
    c=''
elif x[0]=='0' and y[0]=='0' and z[0]=='0':
    c=''
else:
    c='1'
z=c+z

print(z)
