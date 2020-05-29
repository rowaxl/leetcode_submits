from collections import defaultdict
# align text by decreasing order based on the frequency of characters
str1 = 'zoop'         # should be oozp
str2 = 'spicy'        # should be spicy or etc
str3 = 'wombo combo'  # should be oooommbbw c


# hash table
# time: O(n logn)
# space: O(n)
def charFreq(text):
  h = defaultdict(int)
  for ch in text:
    h[ch] += 1

  chs = sorted(h, key=h.get, reverse=True)
  sortedString = ''

  for cha in chs:
    sortedString += (cha * h[cha])

  return sortedString

print(charFreq(str1))
print(charFreq(str2))
print(charFreq(str3))

print('-----')

# valid palindrum
# time: O(n)
# space: O(1)


