
# generating numbered list
from tkinter.tix import INTEGER


numberlist = []
#Big O notation (log N)

x = 0
i = x+1

numberlist = []

for i in range(0,100):
  numberlist.append(i)

y = len(numberlist)

#for y in numberlist:
  #print(y)

#Binary Seaerch Algorithm

def BinarySearch(l, number: int):
  low = 0
  high = len(l)-1
  while low <= high:
    mid =  int((low+high)/2)
    estimate = l[mid]
    if estimate == number:
      return mid
    if estimate > number:
      high = mid - 1
    else:
      low = mid + 1
  return None

b = BinarySearch(numberlist,67)
  
print(b)





