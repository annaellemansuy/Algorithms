
import numpy as np
from collections import deque
from xmlrpc.client import boolean

#Breadth First Search Algorithm
#scenario finding someone that owns a rolls royce from your list of friendsg

graph = {}
#using hash tables
graph["me"] = ["Raphaël", "Jane", "Eduardo"]
graph["Jane"] = ["Sam", "Clover", "Alex"]
graph["Raphaël"] = ["Christopher"]
graph["Sam"] = ["Jane"]
graph["Clover"] = []
graph["Christopher"] = []
graph["Eduardo"] = []

pplwhohaveRollsRoyce = ["Christopher", "Jane"]

# use queue data structure
def search(friend):
  searchqueue = deque() # creates new queue
  searchqueue += graph[friend]
  AlreadySearched = [] # adds an array of all the people searched before
  while searchqueue:
    friend = searchqueue.popleft() #takes first person off the queue
    if not friend in AlreadySearched:
      if friendOwns(friend) == True:
        print(friend + " owns a rolls royce!!!!")
        return True
      else:
        searchqueue += graph[friend]
        AlreadySearched.append(friend)
  return False

def friendOwns(name):
  elementExist = name in pplwhohaveRollsRoyce
  return elementExist
# find people who own rolls royce closest to you
search("Sam")

  






