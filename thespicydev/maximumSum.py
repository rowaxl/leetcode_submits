# find string find the lengh of the longest substring
# e.g. 'hzzdello' -> 'zdel' = 4
# if use linear, time will be O(n ** 3)
# time: O(n)
# space: O(n)

def sliding_window(text) -> int:
  window_left_i = 0
  window_right_i = 0

  chs_in_window = set()
  longest_len = 0

  while window_right_i < len(text):
    while text[window_right_i] not in chs_in_window:
      chs_in_window.add(text[window_right_i])
      window_right_i += 1
      longest_len = max(longest_len, len(chs_in_window))

      if window_right_i >= len(text):
        return longest_len

    while text[window_right_i] in chs_in_window:
      chs_in_window.remove(text[window_left_i])
      window_left_i += 1
  
  return longest_len

print(sliding_window('hzzdelloeazi'))

