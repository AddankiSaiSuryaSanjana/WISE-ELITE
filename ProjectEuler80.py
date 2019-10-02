import math
from decimal import *
def irration_numbers(LIMIT):
    return [i for i in range(2, LIMIT)
                   if int(math.sqrt(i))**2 != i]

def sqrt_of_irrationals(LIMIT):
    for i in irration_numbers(LIMIT):
        getcontext().prec= 101
        yield Decimal(i).sqrt()

def decimal_sum(LIMIT):
    total_decimal_sums = 0
    for i in sqrt_of_irrationals(LIMIT):
        total_decimal_sums += sum(map(int,
                                      str(i)[-100:]))
    return total_decimal_sums

print(decimal_sum(100))
