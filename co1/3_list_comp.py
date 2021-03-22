#3. List comprehensions:

#Generate positive list of numbers from a given list of integers 

numlist=[-10,2,-5,6,-5,7]
poslist=[x for x in numlist if x>0]
print("After removing -ve no.",poslist)

#Square of N numbers

list=[]
n=int(input("Enter the number of numbers:"))
print("Enter ",n,"numbers:")
for x in range(n):
  x=float(input())
  list.append(x)
print(list)
sqlist=[x**2 for x in list]
print(sqlist)

#Form a list of vowels selected from a given word .

vowels=['a','e','i','o','u']
word=str(input("Enter a word: "))
vlist=[x for x in word if x in vowels]
print(vlist)

# List ordinal value of each element of a word

ordword=str(input("Enter a word: "))
ordlist=[ord(x) for x in ordword]
print(ordlist)