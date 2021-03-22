#4.count of words
s=str(input("Enter line of text:"))
count=dict()
words=s.split()
for word in words:
  if word in count:
    count[word]+1
  else:
    count[word]=1
print(count)