# Logistic Regression (built from scratch)
import numpy as np

# Sigmoid Activation Function
def sigmoid(z):
  return 1/(1+np.exp(-z))
  
# Cost Function For Logistic Regression
def costFunction(X,y,theta):
  J = 0
  m = np.size(y)
  grad = 0

  for i in range(0,m):
    h = sigmoid(X[i]*theta.T)
    if y[i] == 0:
      J += (np.log(1-h))
    elif y[i] == 1:
      J+= np.log(h)

    grad += (h-y[i])*X[i]

  J *= 1/m
  grad *= (alpha/m)

  return J,grad

# Dataset
x = np.matrix('1 0;1 1;1 2;1 3;1 4;1 5')
y = np.matrix('0;0;0;1;1;1')
'''
X     Y
--------
0     0
1     0
2     0
3     1
4     1
5     1
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
  return round(float(sigmoid(X*theta.T)))


#================================================#
print("Getting ready to train model")
input("Press [ENTER] to continue")
theta = gradientDescent(1000,x,y)
#================================================#

