from math import sqrt, floor
n=int(input())
primes=[]
powers=[]
divisors=[n]
for i in range(2,floor(sqrt(n)+1)):
    if n%i==0:
        power=0
        while n%i==0:
            power=power+1
            n=n//i
            divisors.append(n)
        primes.append(i)
        powers.append(power)
        divisors.append(i)
        
if n!=1:
    primes.append(n)
    powers.append(1)
    divisors.append(n)
    divisors.append(1)
divisors=set(divisors)
divisors=list(divisors)
divisors.sort()
print(divisors)
print(primes)
print(powers)