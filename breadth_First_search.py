
# Big O notation (no of ppl + no of edges)
import numpy as np
from collections import deque

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
  searchqueue = deque() # creates new queue (queue is empty so far)
  searchqueue += graph[friend] #adds all the people of the person friend list
  AlreadySearched = [] # adds an array of all the people searched before
  while searchqueue: # while searchqueue not empty
    friend = searchqueue.popleft() #takes first person off the queue
    if not friend in AlreadySearched: # if person is not already searched for rolls royce
      if friendOwns(friend) == True:
        print(friend + " owns a rolls royce!!!!")
        return True
      else:
        searchqueue += graph[friend] # add the list of friends' friends to the queue
        AlreadySearched.append(friend) # add checked name to those list of checked people
  return False

def friendOwns(name):
  elementExist = name in pplwhohaveRollsRoyce #checks if the name of the person exists in the array of rollsroyce owners
  return elementExist
# find person who own rolls royce closest to you
search("me")

  






