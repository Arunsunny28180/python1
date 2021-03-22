#20_removing even no.
list1=[]
list2=[]
lim=int(input("enter a lim:"))
print("enter the numbers:")
for i in range(lim):
  list1.append(int(input()))
print("The list is:",list1)
list2.extend(list1)
for i in list1:
  if i%2==0:
    list2.remove(i)
print("after removing even numbers:",list2)    
# sum
s = sum (list1)
print(s)