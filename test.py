from EulerFuncs import primes_below

li = primes_below(350000)
for x in li:
    if x > 304952:
        print x
        break
