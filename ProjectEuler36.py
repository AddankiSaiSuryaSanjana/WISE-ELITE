def is_palindrome(n):
    return str(n)[::-1] == str(n)

def is_binary(n):
    return bin(n).replace("0b", "")

def double_base_palindromes(LIMIT):
    sum_of_double_base_palindromes = 0
    for i in range(1, LIMIT + 1):
        if is_palindrome(i) and is_palindrome(is_binary(i)):
            sum_of_double_base_palindromes += i
    return sum_of_double_base_palindromes

print(double_base_palindromes(1000001))
