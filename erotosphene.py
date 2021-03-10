import datetime
start= datetime.datetime.now()
n=200000
primes=[]
numbers=[True]*(n+1)
numbers[0]=False
numbers[1]=False
for i in range(2,n+1):
    if numbers[i]==True:
        primes.append(i)
        k=i
        while i*k<=n:
            numbers[i*k]=False
            k=k+1 
print(primes)
end= datetime.datetime.now()
print(end-start)

