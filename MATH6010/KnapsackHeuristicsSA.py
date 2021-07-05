# A python3 program to solve the knapsack problem using 
# heuristic approach (Simulated Annealing)

import numpy as np
import random
import math
import copy

def KnapsackHeuristicsSA(W, P, C, T0, alpha, cmax, k):
    bestXL = np.zeros((k,len(W)))
    bestPL = []  # to hold the value of maximum profit from each experiment
    bestWL = []
    # repeat the experiments k times
    for i in range(k):
        T = T0
        n = len(W)  # number of items
        X = np.zeros((n))   # to record the items picked
        bestX = X    # the best solution so far
        curW = sum(X*W)   # current total weight
        curP = sum(X*P)    # current total profit
        bestW = curW   # the best total weight so far, actually useless
        bestP = curP   # the best total profit so far
        count = 0
        while count < cmax:
            j = random.randint(0, n-1)   # pick a random item
            Y = copy.deepcopy(X)
            Y[j] = 1 - X[j]   
            # if the item picked is not already in knapsack 
            # and the knapsack still has capacity for the item picked 
            if (X[j] == 0 and curW + W[j] <= C):
                X = Y    # add the item to knapsack
                curW = curW + W[j]   # add the item's weight to knapsack
                curP = curP + P[j]    # add the item's value to knapsack
                # if this set of items is better then the best found so far
                if curP > bestP:  
                    bestX = X
                    bestW = curW
                    bestP = curP
            # else if the item picked is already in knapsack, use simulated 
            # annealing to decide whether to remove the item from knapsack
            elif X[j] == 1:
                r = random.random()
                threshold = math.exp(-P[j]/T)
                if r < threshold:  
                    X = Y
                    curW = curW - W[j]
                    curP = curP - P[j]
            count += 1
            T = T * alpha  # decrease the temperature
        
        bestXL[i] = bestX
        bestPL.append(bestP)
        bestWL.append(bestW)

    avebestP = sum(bestPL)/len(bestPL)
    avebestW = sum(bestWL)/len(bestWL)

    return bestXL, bestPL, bestWL, avebestP, avebestW


# Driver Code 
if __name__ == '__main__':
    # weight of n items
    W = [70, 73, 77, 80, 82, 87, 90, 94, 98, 106, 110, 113, 115, 118, 120]
    # value of n items
    P = [135, 139, 149, 150, 156, 163, 173, 184, 192, 201, 210, 214, 221, 229, 240]
    C = 750   # knapsack capacity
    T0 = 2000    # initial temperature
    alpha = 0.99999    # temperature decreasing rate
    cmax = 5000   # maximum number of iteration
    k = 5    # number of times to repeat the experiment
    bestXL, bestPL, bestWL, avebestP, avebestW = KnapsackHeuristicsSA(W, P, C, T0, alpha, cmax, k)
    print("optimal set: %s" %(bestXL))
    print("optimal profit: %s" %(bestPL))
    print("optimal weight: %s" %(bestWL))
    print("average optimal profit: %f" %(avebestP))
    print("average optimal weight: %f" %(avebestW))

