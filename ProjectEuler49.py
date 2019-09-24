#ProjectEuler 49
import sympy
def prime_permutations(n):
  if sympy.isprime(n) :
    if sympy.isprime(n + 3330) and sorted(str(n + 3330)) == sorted(str(n)) :
      if sympy.isprime(n + 6660) and sorted(str(n + 6660)) == sorted(str(n)) :
        return True
  return False
def get_twelve_digit_num():
  for i in range(1500, 10000):
    if prime_permutations(i) :
      return str(i) + str(i + 3330) + str(i + 6660)
print(get_twelve_digit_num())
