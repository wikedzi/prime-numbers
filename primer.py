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
   
#print( primeNumbers(299))
