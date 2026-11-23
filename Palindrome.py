word = input(' Enter a word')



right = len(word) - 1
left = 0

while right > left : 

  if word[left] != word[right] :
    print("Nope not a palindrome")

  left = left + 1
  right = right - 1

print(f"yes {word} is a palindrome")