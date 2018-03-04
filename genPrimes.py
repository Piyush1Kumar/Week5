def genPrimes():
""" generator that returns sequence of prime numbers """
    primes = []                 # primes generated so far
    guess = 1                   # next guess number tried
    while True:
        guess += 1
        for p in primes:
            if guess % p == 0:
                break
            else:
                primes.append(guess)
                yield guess