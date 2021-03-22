#6.Store a list of first names. Count the occurrences of ‘a’ within the list

namlist=[]
str1=""
count=0
n=int(input("Enter the number of first names"))
print("Enter",n,"first names:")
for i in range(n):
  name=str(input())
  namlist.append(name)
print(namlist)
for ele in namlist:  
  str1 += ele 
for x in str1:
  if x=="a":
    count+=1
print(count)