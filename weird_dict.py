alphabets = "abcdefghijklmnopqrstuvwxyz"
def wierd_dictionary(length, word):
  return sum([alphabets.find(word[i]) * (26 ** (length - i - 1 )  ) for i in range(length)]) + 1
length = 7
word = 'rishabh'
print(wierd_dictionary(length, word))
