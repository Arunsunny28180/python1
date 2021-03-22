#2.leap year
cyear=2021
upp=int(input("enter a year:"))
if cyear>upp:
 print("please enter a greater year than 2021")
else: 
 print("leap years:")
 for year in range (cyear,upp+1): #comment gfjrh
  if (0==year%4) and (0!=year%100) or (0==year%400):
     print (year)