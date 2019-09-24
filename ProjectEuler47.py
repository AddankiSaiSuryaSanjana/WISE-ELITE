def factorize(n):
  factors = []
  while n > 1 and n % 2 == 0:
    factors.append(2)
    n //= 2
  factor = 3
  while n > 1:
    while n % factor == 0:
      factors.append(factor)
      n //= factor
    factor += 2
  return factors
for i in range(8, 150000):
        if len(set(factorize(i + 3))) == 4 and len(set(factorize(i + 2))) == 4 and len(set(factorize(i + 1))) == 4 and len(set(factorize(i))) == 4:
          print(i)
