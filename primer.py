import time
def primeNumbers(t):
    "This function prints a list of n prime number"
    if t < 2:
        return "Prime numbers starts from 2"
    
    primes = []
    for i in range(2, t):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes

stime = time.time()
print(primeNumbers(1000))
etime = time.time()

print("Start time ", stime, " End time ", etime)
