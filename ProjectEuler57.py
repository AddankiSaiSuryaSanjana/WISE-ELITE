#ProjectEuler57
def continued_fractions():
  numerator = 1
  denominator = 1
  numerator_surplus = 0
  for i in range(1000):
    numerator, denominator = numerator + 2 * denominator, numerator + denominator
    if len(str(numerator)) > len(str(denominator)):
      numerator_surplus += 1
  return numerator_surplus
print(continued_fractions())
