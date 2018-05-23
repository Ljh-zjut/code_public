import numpy as np
import random
GAMMA = 0.1
r = 0.8
Q = np.zeros((16,21))
S = np.zeros((16,2))
A = np.zeros((21,2))

number1 = 0
for a in range(4):
    for b in range(4):
        S[number1] = [200*a+100,200*b+100]
        #S[number1] = [200*a+random.randint(0,200),200*b+random.randint(0,200)]
        number1 += 1

number2 = 0
for c in range(21):
    A[number2] = [10+2*number2,50-2*number2]
    number2 += 1

def getMinQ(state):
    return min(Q[state,:])

def Qlearning(state):
    q1 = S[state,0]
    q2 = S[state,1]
    for action in range(21):
        X1 = q1/(27.5*A[action,0])
        X2 = q2/(27.5*A[action,1])
        diff =  abs(X1 - X2)
        if diff < 0.05:
            reward = 0
        else:
            reward = 1
        Q[state,action]=(1-GAMMA)*Q[state,action]+GAMMA*reward+GAMMA*r*getMinQ(state)
count = 0
while count < 100:
    for i in range(16):
        Qlearning(i)
    count += 1 
print(Q)