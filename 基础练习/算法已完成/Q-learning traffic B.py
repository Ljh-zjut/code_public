import numpy as np
GAMMA = 0.1
r = 0.8
Q = np.zeros((21,21))
A = np.linspace(10,50,num=21)

def getMinQ(state):
    return min(Q[state,:])

def Qlearning(state):
    time2 = A[state]
    for action in range(21):
        time1 = A[action]
        X1 = 700/(27.5*time1)
        X2 = 700/(27.5*time2)
        diff = abs(X1-X2)
        if diff < 0.05 and max(X1,X2) < 0.9:
            reward = 0.9 - max(X1,X2)
        elif diff < 0.05 and max(X1,X2) >= 0.9 and max(X1,X2) < 1:
            reward = 10*(max(X1,X2)-0.9)
        elif diff >= 0.05 or max(X1,X2):
            reward = 1
        Q[state,action]=(1-GAMMA)*Q[state,action]+GAMMA*reward+GAMMA*r*getMinQ(state)

count = 0
while count < 100:
    for i in range(21):
        Qlearning(i)
    count += 1
print(Q)