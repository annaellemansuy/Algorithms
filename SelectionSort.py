#selection sort big O notation O(n^2) not good
#constants are ignored in Big O notation


import random
#generating number list

#random numbered list

def randomNumber(a):
  numberlist = []
  for i in range(0,a):
    n = random.randint(0,10000)
    numberlist.append(n)
  return numberlist   
    

# selectionsSort
def findSmallestNo(l):
  smallest = l[0]
  smallest_i = 0
  for i in range(1,len(l)):
    if l[i] < smallest:
      smallest = l[i]
      smallest_i = i
  return smallest_i

def selectionSort(ar):
  l = ar.copy()
  newList = []
  while len(l) > 0:
    #print(l)
    smallest_i = findSmallestNo(l)
    n = l.pop(smallest_i)
    #print(n)
    newList.append(n)
  return newList

print(selectionSort([2,10,20,6,80,1,0]))
x = randomNumber(10)
print(selectionSort(x))

#print(x)
#k = findSmallestNo(x)
#print(x[k])