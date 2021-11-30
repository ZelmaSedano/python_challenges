def longestWord(str):
  longest = max(str.split(), key=len)
  print(longest)

longestWord('hi there')
