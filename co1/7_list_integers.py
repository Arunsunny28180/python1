#7. Enter 2 lists of integers.

list1=[2,3,4,5]
list2=[1,2,4,8]
list3=[]
#Check (a) Whether list are of same length 
l1=len(list1)
l2=len(list2)
if (l1==l2):
  print("Same length")
else:
  print("length is not same")
#(b) whether list sums to same value
sum1=sum(list1)
sum2=sum(list2)
if(sum1==sum2):
  print("sum is same")
else:
  print("sum is not same")
#(c) whether any value occur in both
for x in list1:
  if x in list2:
    list3.append(x)
print("values occour in both",list3)