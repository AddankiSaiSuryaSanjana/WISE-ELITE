s = 'leetcode'
vowels = 'aeiouAEIOU'
def rev_vowels(s):
  rev_vow_str = ''
  vow_str = ''.join([i for i in s if i in vowels])
  j = len(vow_str) - 1
  for i in s :
    if i in vowels :
      rev_vow_str += vow_str[j]
      j = j - 1
    else :
      rev_vow_str += i
  return rev_vow_str
print(rev_vowels(s))
