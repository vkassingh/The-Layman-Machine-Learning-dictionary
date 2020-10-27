from copy import deepcopy
import random

class State:
  BOTTOM_LESS_PIT = "O"
  GOAL = "$"
  EMPTY = "*"
  USER = "U"

  UP, DOWN, LEFT, RIGHT = 0,1,2,3

  ACTIONS = [ UP, DOWN, LEFT, RIGHT ]

  def __init__(self,grid=False):
    self.grid = [
      [self.GOAL,self.EMPTY,self.EMPTY,self.EMPTY,self.EMPTY],
      [self.EMPTY,self.BOTTOM_LESS_PIT,  self.EMPTY,self.EMPTY, self.EMPTY],
      [self.EMPTY,self.EMPTY,self.BOTTOM_LESS_PIT,self.EMPTY,self.USER],
    ]
    if grid:
      self.grid = grid
    self.userPos = [2,2]

  def __repr__(self):
    string = ""
    string += " "+"- - "*len(self.grid[0]) + "\n"      
    for i in self.grid:
      string += "| "
      string += " | ".join(i) + " |\n"
    string += " "+"- - "*len(self.grid[0])      
    return string

  def __hash__(self):
    return hash(str(self.grid) + str(self.userPos))

def act(state,action):
  def new_pos(state,action):
    pos = [state.userPos[0],state.userPos[1]]
    if action == 0:
      pos[1] = max(0,pos[1]-1)
    elif action == 1:
      pos[1] = min(len(state.grid)-1,pos[1]+1)
    elif action == 2:
      pos[0] = max(0,pos[0]-1)
    elif action == 3:
      pos[0] = min(len(state.grid[0])-1,pos[0]+1)
    return pos
  
  isDone = False
  reward = 0

  if action in (0,1,2,3):
    px,py = new_pos(state,action)
    gridItem = state.grid[py][px]
    newGrid = deepcopy(state.grid)

    if gridItem == state.BOTTOM_LESS_PIT:
      reward = -10
      isDone = True
    elif gridItem == state.EMPTY or gridItem == state.USER:
      reward = -.01
      oldx,oldy = state.userPos
      newGrid[oldy][oldx] = state.EMPTY
      newGrid[py][px] = state.USER
    elif gridItem == state.GOAL:
      isDone = True
      reward = 100
    return newGrid, isDone, reward


def getUser(s):
  for ri in range(0,len(s.grid)):
    if s.USER in s.grid[ri]:
      for i in range(0,len(s.grid[0])):
        if s.grid[ri][i] == s.USER:
          return i, ri
