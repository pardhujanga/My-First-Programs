n=3
primes= [2]
limit=40000

while n<limit or n==limit:
    counter=0
    for i in primes:
        if n%i==0:
            counter+=1
    if counter==0:
        primes.append(n)
    n+=1

print(primes)
