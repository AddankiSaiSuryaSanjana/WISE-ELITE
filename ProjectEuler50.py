#PE 50
import sympy
def consecutive_prime_sum(n):
  sum = 0
  for i in sympy.primerange(2, n) :
    sum += i
    if sum == n:
      return True
  return False
def longest_prime_sum(n):
  for i in range(2, 3940)
  if sympy.isprime(n) and consecutive_prime_sum(n):
    print(n) 
