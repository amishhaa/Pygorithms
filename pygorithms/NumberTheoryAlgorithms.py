import numpy as np
import random

def primeNumbers(n):
    if n <= 1:
        return []
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, is_prime in enumerate(sieve) if is_prime]

def euclideanAlgorithm(a, b): 
    while b:
        a, b = b, a % b
    return a

def extendedEuclideanAlgorithm(a, b):
    x, y, u, v = 0, 1, 1, 0
    while b:
        q, r = divmod(a, b)
        a, b = b, r
        x, y, u, v = u, v, x - q*u, y - q*v
    return a, x, y

def eulerTotientFunction(n):
    primes, _ = primeNumbers(n + 1)
    totient = n
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            totient -= totient // p
            while n % p == 0:
                n //= p
    if n > 1:
        totient -= totient // n
    return totient

def modularExponentiation(base, exponent, modulus):
    result = 1
    base %= modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result

def millerRabinPrimalityTest(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = modularExponentiation(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True

def chineseRemainderTheorem():
    M = 1
    for mi in m:
        M *= mi
    Ml = [M // mi for mi in m]
    S = [0] * len(m)
    for i, mi in enumerate(m):
        t = Ml[i]
        while t % mi != 1:
            t += M
        S[i] = t
    x = 0
    for i in range(len(a)):
        x = (x + a[i] * Ml[i] * S[i]) % M
    return x

def segmentedSieve():
    limit = int(n**0.5)
    sieve = [True] * (limit + 1)  # Sieve for small primes
    sieve[0] = sieve[1] = False

  # Generate primes up to the square root of n
    for i in range(2, limit + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    segment_size = limit // 10 + 1  # Adjust segment size for efficiency
    primes = [p for p in range(2, limit + 1) if sieve[p]]
    segments = [False] * (segment_size + 1)

  # Handle divisibility by small primes in segments
    for p in primes:
        if p * p > n:
            break
    base = (p // segment_size) * segment_size
    for i in range(base, n + 1, segment_size):
        segments[i % segment_size] = True
    for i in range(limit + 1, n + 1, segment_size):
        copy = segments.copy()
        for p in primes:
            if p * p > i:
                break
            d = (i // p) * p
            while d < i:
                d += p
        copy[(d - i) % segment_size] = False
        primes.extend([i + offset for offset, is_prime in enumerate(copy) if is_prime])
    return primes

def fastFourierTransform():
    N = len(x)
    if N <= 1: return x
    even = fastFourierTransform(x[0::2])
    odd = fastFourierTransform(x[1::2])
    T = [np.exp(-2j * np.pi * k / N) * odd[k % (N//2)] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

def monteCarloAlgorithm():
    inside_circle = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x**2 + y**2 <= 1:
            inside_circle += 1
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate