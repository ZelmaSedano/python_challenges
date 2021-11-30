def vowelCount(str):
  count = 0

  vowel = set('aeiouAEIOU')

  for alphabet in str:
    if alphabet in vowel:
      count += 1
  
  print('No. of vowels: ', count)

vowelCount('hi')
