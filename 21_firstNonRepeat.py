def firstNonRepeat(str):
  char_order = []
  counts = {}
  for c in str:
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1
      char_order.append(c)
  
  for c in char_order:
    if counts[c] == 1:
      return c
  return None

print(firstNonRepeat('hih'))
