# A python3 program to find solutions to the Kirkman Schoolgirl problem
# with heuristic approach (Tabu search)

import numpy as np
import random
import math
import timeit
import copy

# neighborhood search using tabu search approach
def NBSTabu(S, Q, feasibleNB, cost):
    n = len(feasibleNB) 
    # randomly choose a tuple as base case, 
    # in which i0 and j0 are not in the same team
    okchoice = False
    tupley = ()
    k0 = None
    i0 = None
    j0 = None
    while okchoice != True:  
        k = random.sample(list(range(n)),1)[0]
        choice = feasibleNB[k]
        tupley = choice
        k0 = tupley[0]
        i0 = tupley[1]
        j0 = tupley[2]
        si0 = S[k0][i0]   # s for student
        sj0 = S[k0][j0]
        teami0 = i0 // 3  
        teamj0 = j0 // 3
        if teami0 != teamj0:
           okchoice = True
    # get the new frequency matrix and total cost for base case
    Qy, costy = getQNC(S, Q, k0, i0, j0, cost)
    for combn in feasibleNB:
        k = combn[0]
        i = combn[1]
        j = combn[2]
        # get the new frequency matrix and total cost for current 3-tuple change
        Qyy, costyy = getQNC(S, Q, k, i, j, cost)
        if costyy < costy:
            Qy = Qyy
            costy = costyy
            tupley = combn
    return Qy, costy, tupley


# get the frequency matrix and total cost based on the inputs
def getQNC(S, Q, k, i, j, cost):
    teami = i // 3   # the team i is in
    teamj = j // 3   # the team j is in
    if teami == teamj:
        return Q, cost   
    si = S[k][i]   # student at position i on day k 
    sj = S[k][j]   # student at position j on day k
    n = len(Q)
    Qy = np.copy(Q)
    costy = copy.deepcopy(cost)
   # iterature through each student in teami and teamj
    for r in range(3):
        pi = S[k][teami*3+r]    # student in teami, p for partner
        pj = S[k][teamj*3+r]    # student in teamj
        if pi != si:
            # minus the relevant costs before the swapping
            costy = costy - abs(Qy[si][pi]-1) - abs(Qy[pi][si]-1) \
                - abs(Qy[sj][pi]-1) - abs(Qy[pi][sj]-1)
            # update the frequency matrix if swapping is to be done
            Qy[si][pi] += -1
            Qy[pi][si] += -1
            Qy[sj][pi] += 1
            Qy[pi][sj] += 1
            # add back those relevant costs after the swapping
            costy = costy + abs(Qy[si][pi]-1) + abs(Qy[pi][si]-1) \
                + abs(Qy[sj][pi]-1) + abs(Qy[pi][sj]-1)
        if pj != sj: 
            costy = costy - abs(Qy[sj][pj]-1) - abs(Qy[pj][sj]-1) \
                - abs(Qy[si][pj]-1) - abs(Qy[pj][si]-1)  
            Qy[sj][pj] += -1 
            Qy[pj][sj] += -1 
            Qy[si][pj] += 1
            Qy[pj][si] += 1
            costy = costy + abs(Qy[sj][pj]-1) + abs(Qy[pj][sj]-1) \
                + abs(Qy[si][pj]-1) + abs(Qy[pj][si]-1)  
        # input("Press Enter to continue...")
    return Qy, costy  


# main function
def KirkmanSchoolgirl(n, L, cmax):
    start = timeit.default_timer()
    days = (n-1)//2   # number of days required 
    # initialize a random schedule matrix 
    S = np.array([random.sample(list(range(n)), n) for i in range(days)])
    S0 = np.copy(S)
    # initialize a frequency matrix to record the number of times 
    # each student teamed with other students in the current schedule
    Q = np.zeros((n,n)) 
    for i in range(n):  # iterate through each student
        for j in range(days):  # iterate through each day
            s, = np.where(S[j]==i)
            team = s//3  # get the team of the student
            # iterate through each team partner of student i on day k
            for k in range(3):
                partner = S[j][team*3+k]
                if partner != i:
                    Q[i][partner] += 1
    # calculate the objective cost for current schedule
    cost = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                cost += abs(Q[i][j]-1) 
    # Create a list of 3-element tuples for all possible swaps
    # k = which day; i,j = the indexes of the two students to be swapped on day k
    allNB = []
    for k in range(days):
        for i in range(n):
            for j in range(i+1, n, 1):
                pair = (k,i,j)
                allNB.append(pair)
    feasibleNB = allNB  # to record feasible neighbours
    
    # Tabu search
    # Create a Tabu List
    TabuList = []
    # feasibleNB = set(allNB) - set(TabuList)
    bestS = S
    bestQ = Q
    bestcost = cost
    count = 0
    # keep iterating until either reaching max number of counts 
    # or optimal solution is found
    while count < cmax:
        Q, cost, choice = NBSTabu(S, Q, feasibleNB, cost)  # find best neighbour in neighbourhood
        k = choice[0]  # day k 
        i = choice[1]  
        j = choice[2]
        # swap student at index i and student at index j on day k
        temp = S[k][i]
        S[k][i] = S[k][j]
        S[k][j] = temp
        if cost == 0:
            stop = timeit.default_timer()
            print('Time: ', stop - start)  
            return S0, S, Q, cost
        # Here we treat TabuList as a queue with length L
        TabuList.append(choice)  # add the current choice to end of TabuList
        feasibleNB.remove(choice)  # remove the current choice from feasible neighbours
        # add the 3-tuple back to feasibleNb after L iteration
        if len(TabuList) > L:
            feasibleNB.append(TabuList.pop(0)) 
        if cost < bestcost:
            bestcost = cost
            bestS = S
            bestQ = Q
        count += 1
        print(count)
        print(cost)

    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    return S0, bestS, bestQ, bestcost


# Driver Code 
if __name__ == '__main__':
    L = 30   # length of TabuList
    cmax = 10000   # maximum number of iterations
    n = 15   # number of students, n = 6k+3, k is any positive integer
    S0, bestS, bestQ, bestcost = KirkmanSchoolgirl(n, L, cmax)
    print(S0)  # inital schedule
    print(bestS)  # best schedule
    print(bestQ)  # frequency matrix according to bestS
    print(bestcost)  # cost according to bestS
