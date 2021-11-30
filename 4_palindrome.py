def checkPalindrome(str):
  reversed_str = str[::1]
  
  if(str==reversed_str):
    print('palindrome')
  else:
    print('not a palindrome')

checkPalindrome('hi')
