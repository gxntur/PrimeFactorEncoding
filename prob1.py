"""
Compsci 320 Assignment 1, finding PFE prime factor encoding
Author: William Guntur
Problem 1, Prime factor encoding
We aim to find every number as a product of only prime numbers, while referring
to the prime numbers by their ascending order.
"""
import math
import collections
import sys

#Primes is a list of primes in order of appearance.
def pfe(step):
    print("  k pfe(k)")
    primes = []
    encodedprimes = []
    for i in range(1, int(step)+1):
        if isPrime(i):
            primes.append(i)
            print('{:>3}'.format(str(i)) + " " + str(primes.index(i)+1))
        else:
            #print(getPrimeFactors(i))
            encodedprimes = getPFEncoding(getPrimeFactors(i), primes)
            c = collections.Counter(encodedprimes)
            result = []
            for key, value in c.items():
                if value > 1:
                    result += [str(key) + '^' + str(value)]
                else:
                    result += [str(key)]
            final = ''
            final += str(result.pop(0))
            for j in result:
                final += '*'
                final += str(j)
            print('{:>3}'.format(str(i)) + " " + final)
            
            

            

def getFactors(n):
    factors = []
    for x in range(2, math.ceil(math.sqrt(n)+1)):
        if n%x == 0:
            if isPrime(x):
                factors.append(x)
            else:
                factors.append(x)
                factors.append(getFactors(n/x))
    return factors

def getPrimeFactors(n):
    a = 2
    factors = []
    while a * a <= n:
        if (n % a):
            a += 1
        elif n % a == 0:
            factors.append(a)
            n //= a
    factors.append(n)
    return(factors)

def getPFEncoding(primeFactors, primes):
    encoded = []
    for i in primeFactors:
        encoded.append(primes.index(i) + 1)

    return encoded

    
            

            
        
#Determines if a number is a prime or not
def isPrime(n):
    if n<1:
        return False
    if n == 1:
        return True
    if n%2 ==0:
        if n == 2:
            return True
        else:
            return False
    #The fastest way to determine a prime is to divide up to the square root of the number
    for x in range(2, math.ceil(math.sqrt(n)+1)):
        if n%x==0:
            return False
    return True
        
        
def main():
    """
    for line in sys.stdin:
        pfe(str(line))
        break
    """
    pfe(input())

main()
