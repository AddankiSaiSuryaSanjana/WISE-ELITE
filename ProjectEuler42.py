import string
A2Z = string.ascii_uppercase
tri_encoding = {a: b for a, b in zip(A2Z, range(1, 27))}
print(tri_encoding)

def word_value(n : int)->bool:
    return sum([tri_encoding[ch] for ch in s])

def is_triangular(n : int)->bool:
    r = 1
    while r * (r + 1) < 2 * n:
        r += 1
    return r * (r + 1) == 2 * n

def is_triangular_word(s : str)->bool:
    return int(is_triangular(word_value(s)))

#num_of_triangular_words = sum([is_triangular_word(line.strip()) for line in open("InputFile.txt")])
