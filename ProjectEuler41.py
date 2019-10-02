#PE41
#NineDigitNumbers(1+2+3+4+5+6+7+8+9=45) => div by 3 => Not a prime
#EightDigitNumbers(1+2+3+4+5+6+7+8=36)  => div by 3 => Not a prime
#SixDigitNumbers(1+2+3+4+5+6=21)  => div by 3 => Not a prime
from itertools import permutations
import sympy
def pandigital_prime(n):
  p = permutations(['7', '6', '5', '4', '3', '2', '1' ], n)
  for i in p:
    if sympy.isprime(int(''.join(list(i)))):
      return int(''.join(list(i)))
print(pandigital_prime(7))
