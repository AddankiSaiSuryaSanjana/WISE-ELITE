def triangular_numbers(n):
    return int((n * (n + 1)) / 2)

def is_pentagonal(n) : 
    i = 1
    while True: 
        pentagon_num = (i * (3 * i - 1)) / 2
        i += 1
        if (pentagon_num >= n): 
            break      
    return (pentagon_num == n)

def is_hexagonal(n) : 
    i = 1
    while True:  
        hexagon_num = i * (2 * i - 1)
        i += 1
        if (hexagon_num >= n): 
            break 
    return (hexagon_num == n)

def next_triangular_number(LIMIT):
    for i in range(20000, LIMIT):
        k = triangular_numbers(i)
        if is_pentagonal(k) and is_hexagonal(k):
            print(k)

next_triangular_number(30000)
