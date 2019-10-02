def is_prime(n):
    if n in [2, 3, 5, 7]:
        return True
    if n % 2 == 0:
        return False
    r = 3
    while r * r <= n :
        if n % r == 0:
            return False
        r += 2
    return True

def reverse(n):
    return int(reversed(str(n)))

def left_trunctable_prime(n):
    c = 0
    for i in range(len(str(n))):
        if is_prime(int(str(n)[i:])):
            print(int(str(n)[i:]))
            c += 1
    if c == len(str(n)):
        return True
    return False

def right_trunctable_prime(n):
    c = 0
    for i in range(len(str(n))):
        if is_prime(int(str(n)[:len(str(n)) - i])):
            print(int(str(n)[:len(str(n)) - i]))
            c += 1
    if c == len(str(n)):
        return True
    return False
    
print(left_trunctable_prime(3797))
print(right_trunctable_prime(3797))
