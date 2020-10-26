from environment import State, getUser, act
import numpy as np
import random

random.seed(42)

N_STATES = 4
N_EPISODES = 20000
MIN_ALPHA = 0.2

alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)
gamma = 1.0
eps = 0.4

print(State())

qTable = {}

def q(state, action=None): 
  if state not in qTable:
    qTable[state] = np.zeros(len(state.ACTIONS))  
  if action is None:
    return qTable[state]
    
  return qTable[state][action]

def choose_action(state):
  if random.uniform(0, 1) < eps:
    return random.choice(state.ACTIONS) 
  else:
    return np.argmax(q(state))

for e in range(N_EPISODES):
  state = State()
  total_reward = 0
  alpha = alphas[e]
  done = False
    
  while not done:
    action = choose_action(state)
    next_state, done, reward = act(state, action)
    next_state = State(next_state)
    total_reward += reward
        
    q(state)[action] = q(state, action) + alpha * (reward + gamma *  np.max(q(next_state)) - q(state, action))
    state.grid = next_state.grid
    state.userPos = getUser(state)

  print(f"Episode {e+1} --> {total_reward}")

while not done:
  action = np.argmax(q(state))
  next_state, done, reward = act(state, action)
  next_state = State(next_state)
  total_reward += reward
        
  q(state)[action] = q(state, action) + alpha * (reward + gamma *  np.max(q(next_state)) - q(state, action))
  state.grid = next_state.grid
  state.userPos = getUser(state)

print("Score : "+str(total_reward))
