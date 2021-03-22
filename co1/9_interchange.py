#9. Create a string from given string where first and last characters exchanged.

word=str(input("Enter a word:"))
copy=word
word=word[-1:] + word[1:-1] + word[:1]
print(copy,"--",word)