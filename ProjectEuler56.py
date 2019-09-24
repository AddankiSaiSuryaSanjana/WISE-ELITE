#ProjectEuler 56
def individual_sum(n):
  return sum([int(i) for i in str(n)])
def powerful_digit_sum():
  return max([individual_sum(i**j) for i in range(1, 100) for j in range(1, 100)])
powerful_digit_sum()
