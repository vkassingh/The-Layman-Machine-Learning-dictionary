# Linear Regression
import numpy as np
  
# Cost Function For Linear Regression
def costFunction(X,y,theta):
  J = 0
  m = np.size(y)
  grad = 0

  for i in range(0,m):
    h = X[i]*theta.T

    grad += (h-y[i])*X[i]

  J *= 1/m
  grad *= (alpha/m)

  return J,grad

# Dataset
x = np.matrix('1 0;1 100;1 200;1 300;1 400;1 500')
y = np.matrix('0;1;2;3;4;5')
'''
X     Y
--------
0     0
100   1
200   2
300   3
400   4
500   5
'''
# Learning rate
alpha = .3

# Optimization algorithm
def gradientDescent(iterations,x,y):
  # Initial Value for theta
  theta = np.matrix('0.0 0.0')
  # Initializing new Cost and Old Cost
  cost = costFunction(x,y,theta)[0]
  oldCost = 10000
  # Use the gradient while the threshold is not reached
  for iteration in range(0,iterations):
    gradient = costFunction(x,y,theta)[1]
    print(f"Iteration {iteration} :",theta,oldCost,cost)

    theta -= gradient
    oldCost = cost
    cost = costFunction(x,y,theta)[0]

  return theta

# Predicting function
def predict(x,theta):
  X = np.matrix(f'1 {x}')
  return round(float(X*theta.T))


#================================================#
print("Getting ready to train model")
input("Press [ENTER] to continue")
theta = gradientDescent(1000,x,y)
#================================================#

