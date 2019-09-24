import sympy
def is_num_square(n):
  for i in range(0, n // 2 + 1):
    if n == i * i:
      return True
  return False
def is_primes(n):
  for j in sympy.primerange(1,n):
      if is_num_square((n - j) // 2):
        return True
  return False

def goldbach_conjecture():
  for i in range(3, 40, 2):
    if (not sympy.isprime(i)) and is_primes(i):
      print(i)
goldbach_conjecture()    
