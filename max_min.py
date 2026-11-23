# Maximum and minimum — Find the maximum and minimum element of a list without using max() or min().

list1 = [10 , 20 , 90 , 76 , 1002 , 9898]

small = list1[0]
maxi = list1[0]

for x in list1:
  if x < small:
    small = x

  if x > maxi : 
    maxi = x

  

print(f"Smallest value is {small}")
print(f"Largest  value is {maxi}")