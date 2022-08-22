# quicksort Big O notation (nlogn) (avg case)
# worst case Big O (n^2)

import random
#generating number list

#random numbered list

def randomNumber(a: int):
  numberlist = []
  for i in range(0,a):
    n = random.randint(0,10000)
    numberlist.append(n)
  return numberlist   
    
#quick sort algorithm
def quicksort(b):
  if len(b) < 2 :
    return b
  else:
    pivot = b[0]
    less = [b for b in b[1:] if b <= pivot]
    more = [b for b in b[1:] if b >= pivot]
  return quicksort(less) + [pivot] + quicksort(more)


print(quicksort(randomNumber(10)))
