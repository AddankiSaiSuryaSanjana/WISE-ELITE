import math
from itertools import combinations
from fractions import Fraction
def proper_fraction(d):
  comb = [i for i in range(1, d)]
  fractions = combinations(comb, 2)
  for i in fractions :
    if math.gcd(i[0], i[1]) == 1:
      yield Fraction(i[0], i[1])

print(sorted(proper_fraction(8)).index(Fraction(3, 7)))
print(proper_fraction(8))	
