# A python3 program to solve the knapsack problem through exhausive search

import numpy as np

def KnapsackExhaustive(W, P, C):
    n = len(W)
    maxPerm = 2**n
    S = np.zeros((maxPerm,n))
    setW = []
    setP = [] 
    for i in range(maxPerm):
        s = bin(i)[2:]
        s = '0'*(n-len(s))+s
        S[i] = list(map(int,list(s)))
    setW = np.sum(S * W, axis=1)
    setP = np.sum(S * P, axis=1)
    
    feasibleSet = (np.array(setW) <= C)
    feasibleX = S[feasibleSet]
    feasibleW = setW[feasibleSet]
    feasibleP = setP[feasibleSet]
    bestP = np.amax(feasibleP)
    ind = np.where(feasibleP == bestP)
    bestX = feasibleX[ind]
    bestW = feasibleW[ind]
    print(len(feasibleX))
    return bestX, bestP, bestW



# Driver Code 
if __name__ == '__main__':
    W = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    P = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    C = 750
    bestX, bestP, bestW = KnapsackExhaustive(W, P, C)
    print("optimal set: %s" %(bestX))
    print("optimal profit: %s" %(bestP))
    print("optimal weight: %s" %(bestW))
